import random
from datetime import datetime

import pandas as pd
import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Attendance & Performance Analytics",
    page_icon="🌷",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# STYLE
# =========================================================

st.html(
    """
    <style>
        :root {
            --ink: #3c3038;
            --muted: #7e6c76;
            --berry: #95516f;
            --rose: #df88a6;
            --peach: #f6cbb8;
            --lavender: #d8cdf0;
            --line: #eadfe4;
        }

        .stApp {
            background:
                radial-gradient(circle at 7% 7%, rgba(246,203,184,.42), transparent 24%),
                radial-gradient(circle at 92% 9%, rgba(216,205,240,.50), transparent 25%),
                radial-gradient(circle at 85% 80%, rgba(223,136,166,.17), transparent 22%),
                linear-gradient(180deg, #fffdfc 0%, #fff7fa 50%, #fffaf7 100%);
        }

        .block-container {
            max-width: 1240px;
            padding-top: 5.1rem;
            padding-bottom: 4rem;
        }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        div.stButton > button,
        div.stDownloadButton > button {
            min-height: 46px;
            border: none;
            border-radius: 14px;
            color: white;
            font-weight: 700;
            background: linear-gradient(135deg, #884761, #c4698b);
            box-shadow: 0 8px 20px rgba(136,71,97,.20);
        }

        div.stButton > button:hover,
        div.stDownloadButton > button:hover {
            color: white;
            border: none;
            background: linear-gradient(135deg, #783b54, #ae587a);
        }

        div[data-testid="stDataFrame"] {
            border: 1px solid var(--line);
            border-radius: 18px;
            overflow: hidden;
            box-shadow: 0 8px 22px rgba(105,63,82,.055);
            background: white;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: .4rem;
            padding: .35rem;
            border: 1px solid var(--line);
            border-radius: 15px;
            background: rgba(255,255,255,.70);
        }

        .stTabs [data-baseweb="tab"] {
            height: 42px;
            border-radius: 11px;
            padding-left: 1rem;
            padding-right: 1rem;
            color: #755866;
            font-weight: 650;
        }

        .stTabs [aria-selected="true"] {
            color: white !important;
            background: linear-gradient(135deg, #884761, #bd6285) !important;
        }

        .stTabs [data-baseweb="tab-highlight"] {display: none;}

        @media (max-width: 800px) {
            .block-container {
                padding-top: 5rem !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }
            .stTabs [data-baseweb="tab-list"] {
                overflow-x: auto;
                flex-wrap: nowrap;
            }
        }
    </style>
    """
)


# =========================================================
# UI HELPERS
# =========================================================

def hero():
    st.html(
        """
        <div style="
            position:relative; overflow:hidden; padding:32px;
            border-radius:28px; border:1px solid rgba(149,81,111,.13);
            background:linear-gradient(135deg,rgba(255,255,255,.97),rgba(255,240,246,.92));
            box-shadow:0 18px 42px rgba(110,62,84,.10); margin-bottom:14px;
        ">
            <div style="
                position:absolute; width:240px; height:240px; border-radius:50%;
                right:-75px; top:-78px;
                background:linear-gradient(135deg,rgba(232,154,181,.42),rgba(205,190,238,.48));
            "></div>

            <div style="
                position:relative; z-index:2; display:inline-block;
                padding:7px 12px; border-radius:999px;
                background:rgba(149,81,111,.09); color:#8d4b69;
                font-size:12px; font-weight:800; margin-bottom:16px;
            ">
                🌷 PEOPLE ANALYTICS PORTFOLIO
            </div>

            <div style="
                position:relative; z-index:2; max-width:880px;
                color:#3c3038; font-size:clamp(38px,6vw,62px);
                line-height:1.03; font-weight:800; letter-spacing:-2px;
            ">
                Attendance & Performance Analytics
            </div>

            <div style="
                position:relative; z-index:2; max-width:780px;
                margin-top:17px; color:#7e6c76; font-size:16px; line-height:1.7;
            ">
                An interactive workspace for exploring attendance patterns,
                employee performance, department trends, and records that may need attention.
            </div>

            <div style="
                position:relative; z-index:2; display:flex; flex-wrap:wrap;
                gap:8px; margin-top:18px;
            ">
                <span style="padding:7px 11px;border-radius:999px;background:white;border:1px solid #eadfe4;color:#684f5b;font-size:13px;font-weight:650;">Attendance analysis</span>
                <span style="padding:7px 11px;border-radius:999px;background:white;border:1px solid #eadfe4;color:#684f5b;font-size:13px;font-weight:650;">Performance metrics</span>
                <span style="padding:7px 11px;border-radius:999px;background:white;border:1px solid #eadfe4;color:#684f5b;font-size:13px;font-weight:650;">Department comparison</span>
                <span style="padding:7px 11px;border-radius:999px;background:white;border:1px solid #eadfe4;color:#684f5b;font-size:13px;font-weight:650;">Python + Streamlit</span>
            </div>
        </div>
        """
    )


def section(kicker, title, description):
    st.html(
        f"""
        <div style="margin-top:25px;margin-bottom:13px;">
            <div style="color:#b15d82;font-size:12px;font-weight:800;letter-spacing:1.4px;margin-bottom:7px;">
                {kicker.upper()}
            </div>
            <div style="color:#3c3038;font-size:31px;line-height:1.15;font-weight:800;letter-spacing:-.8px;">
                {title}
            </div>
            <div style="margin-top:8px;color:#7e6c76;font-size:15px;line-height:1.65;max-width:860px;">
                {description}
            </div>
        </div>
        """
    )


def metric_card(label, value, caption, accent):
    return f"""
    <div style="
        position:relative;overflow:hidden;min-height:118px;padding:18px;
        border-radius:21px;background:rgba(255,255,255,.91);
        border:1px solid #eadfe4;box-shadow:0 9px 22px rgba(104,64,82,.065);
    ">
        <div style="
            position:absolute;width:64px;height:64px;border-radius:50%;
            right:-18px;top:-18px;background:{accent};opacity:.55;
        "></div>
        <div style="position:relative;z-index:2;color:#8b7580;font-size:12px;font-weight:650;">{label}</div>
        <div style="position:relative;z-index:2;margin-top:8px;color:#7b4061;font-size:31px;line-height:1;font-weight:800;">{value}</div>
        <div style="position:relative;z-index:2;margin-top:9px;color:#9a8590;font-size:11px;">{caption}</div>
    </div>
    """


def render_bar(label, value, maximum):
    width = 0 if maximum == 0 else value / maximum * 100
    st.html(
        f"""
        <div style="
            padding:16px;border-radius:18px;border:1px solid #eadfe4;
            background:rgba(255,255,255,.88);margin-bottom:9px;
            box-shadow:0 7px 18px rgba(104,64,82,.045);
        ">
            <div style="display:flex;justify-content:space-between;gap:10px;margin-bottom:8px;">
                <div style="color:#49363f;font-size:13px;font-weight:700;">{label}</div>
                <div style="color:#934c70;font-size:13px;font-weight:800;">{value}</div>
            </div>
            <div style="height:9px;border-radius:999px;background:#f0e6eb;overflow:hidden;">
                <div style="
                    width:{width:.1f}%;height:100%;border-radius:999px;
                    background:linear-gradient(90deg,#ad587d,#e58eab,#ccb3ec);
                "></div>
            </div>
        </div>
        """
    )


# =========================================================
# SAMPLE DATA
# =========================================================

@st.cache_data
def build_sample_data():

    random.seed(88)

    employees = [
        (f"EMP-{i:03d}", f"Employee {i:03d}")
        for i in range(1, 121)
    ]

    departments = [
        "Administration",
        "Finance",
        "Human Resources",
        "Operations",
        "General Affairs",
        "Data & Reporting",
    ]

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
    ]

    rows = []

    for employee_id, employee_name in employees:

        department = random.choice(departments)
        base_performance = random.uniform(72, 94)

        for month_number, month in enumerate(months, start=1):

            working_days = random.choice([20, 21, 22, 23])

            absent_days = random.choices(
                [0, 1, 2, 3, 4],
                weights=[48, 28, 14, 7, 3],
            )[0]

            leave_days = random.choices(
                [0, 1, 2, 3],
                weights=[55, 28, 13, 4],
            )[0]

            late_count = random.choices(
                list(range(0, 9)),
                weights=[22, 20, 17, 14, 10, 7, 5, 3, 2],
            )[0]

            present_days = max(
                0,
                working_days - absent_days - leave_days,
            )

            attendance_rate = (
                present_days / working_days * 100
            )

            performance_noise = random.uniform(-7, 7)

            performance_score = (
                base_performance
                + (attendance_rate - 90) * 0.20
                - late_count * 0.45
                + performance_noise
            )

            performance_score = max(
                55,
                min(100, performance_score),
            )

            target_achievement = (
                performance_score
                + random.uniform(-8, 8)
            )

            target_achievement = max(
                50,
                min(110, target_achievement),
            )

            workload = random.choice(
                ["Low", "Moderate", "High"]
            )

            if performance_score >= 85:
                evaluation_status = "Strong"
            elif performance_score >= 75:
                evaluation_status = "On Track"
            else:
                evaluation_status = "Needs Attention"

            rows.append(
                {
                    "employee_id": employee_id,
                    "employee_name": employee_name,
                    "department": department,
                    "month": month,
                    "month_number": month_number,
                    "working_days": working_days,
                    "present_days": present_days,
                    "late_count": late_count,
                    "leave_days": leave_days,
                    "absent_days": absent_days,
                    "attendance_rate": round(attendance_rate, 2),
                    "performance_score": round(performance_score, 2),
                    "target_achievement": round(target_achievement, 2),
                    "workload": workload,
                    "evaluation_status": evaluation_status,
                }
            )

    return pd.DataFrame(rows)


# =========================================================
# FILE INPUT
# =========================================================

REQUIRED_COLUMNS = [
    "employee_id",
    "employee_name",
    "department",
    "month",
    "month_number",
    "working_days",
    "present_days",
    "late_count",
    "leave_days",
    "absent_days",
    "attendance_rate",
    "performance_score",
    "target_achievement",
    "workload",
    "evaluation_status",
]


def read_file(uploaded_file):
    name = uploaded_file.name.lower()

    if name.endswith(".csv"):
        return pd.read_csv(uploaded_file)

    if name.endswith(".xlsx") or name.endswith(".xls"):
        return pd.read_excel(uploaded_file)

    raise ValueError("Please upload a CSV or Excel file.")


# =========================================================
# APP
# =========================================================

hero()

st.caption(
    "This portfolio project uses synthetic employee records. "
    "No confidential personnel data is included."
)

section(
    "Input",
    "Explore the employee dataset",
    "Start with the built in sample or upload a dataset with the same structure.",
)

source = st.radio(
    "Data source",
    ["Use sample data", "Upload a file"],
    horizontal=True,
    label_visibility="collapsed",
)

data = None

if source == "Use sample data":
    data = build_sample_data()
    st.success(
        f"Sample data ready. {len(data):,} monthly employee records loaded."
    )
else:
    uploaded_file = st.file_uploader(
        "Upload CSV or Excel",
        type=["csv", "xlsx", "xls"],
    )

    if uploaded_file is not None:
        try:
            data = read_file(uploaded_file)
            st.success(f"{uploaded_file.name} loaded.")
        except Exception as error:
            st.error(str(error))

if data is None:
    st.info("Choose the sample data or upload a file to continue.")
    st.stop()

missing_columns = [
    column
    for column in REQUIRED_COLUMNS
    if column not in data.columns
]

if missing_columns:
    st.error(
        "Missing required columns: "
        + ", ".join(missing_columns)
    )
    st.stop()


# =========================================================
# FILTERS
# =========================================================

section(
    "Analysis",
    "Filter the view",
    "Use department and month filters to focus the analysis on a specific group or period.",
)

filter_one, filter_two = st.columns(2)

with filter_one:
    department_options = sorted(
        data["department"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_departments = st.multiselect(
        "Department",
        department_options,
        default=department_options,
    )

with filter_two:
    month_lookup = (
        data[["month", "month_number"]]
        .drop_duplicates()
        .sort_values("month_number")
    )

    month_options = month_lookup["month"].tolist()

    selected_months = st.multiselect(
        "Month",
        month_options,
        default=month_options,
    )

filtered = data[
    data["department"].isin(selected_departments)
    &
    data["month"].isin(selected_months)
].copy()

if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()


# =========================================================
# SUMMARY
# =========================================================

employees = filtered["employee_id"].nunique()
avg_attendance = filtered["attendance_rate"].mean()
avg_performance = filtered["performance_score"].mean()
avg_late = filtered["late_count"].mean()

attention_count = filtered.loc[
    filtered["evaluation_status"] == "Needs Attention",
    "employee_id",
].nunique()

correlation = filtered[
    ["attendance_rate", "performance_score"]
].corr().iloc[0, 1]

section(
    "Overview",
    "People analytics snapshot",
    "A compact summary of attendance, performance, punctuality, and employee records that may need attention.",
)

cards = (
    """
    <div style="
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(170px,1fr));
        gap:11px;
        margin:16px 0 22px 0;
    ">
    """
    + metric_card(
        "Employees",
        f"{employees:,}",
        "Unique employees",
        "#f6c5d6",
    )
    + metric_card(
        "Attendance rate",
        f"{avg_attendance:.1f}%",
        "Average attendance",
        "#d9d2f3",
    )
    + metric_card(
        "Performance",
        f"{avg_performance:.1f}",
        "Average score",
        "#f6cbb7",
    )
    + metric_card(
        "Late frequency",
        f"{avg_late:.1f}",
        "Average per record",
        "#f2bed0",
    )
    + metric_card(
        "Needs attention",
        f"{attention_count:,}",
        "Unique employees",
        "#dabfea",
    )
    + "</div>"
)

st.html(cards)


# =========================================================
# TABS
# =========================================================

tab_overview, tab_department, tab_relationship, tab_attention, tab_data = st.tabs(
    [
        "Overview",
        "Department view",
        "Attendance vs performance",
        "Attention list",
        "Data",
    ]
)


# =========================================================
# OVERVIEW TAB
# =========================================================

with tab_overview:

    left, right = st.columns(2)

    with left:
        st.subheader("Evaluation status")

        status_counts = (
            filtered["evaluation_status"]
            .value_counts()
            .reindex(
                ["Strong", "On Track", "Needs Attention"],
                fill_value=0,
            )
        )

        maximum = int(status_counts.max())

        for label, value in status_counts.items():
            render_bar(
                label,
                f"{int(value):,}",
                maximum if maximum else 1,
            )

    with right:
        st.subheader("Workload mix")

        workload_counts = (
            filtered["workload"]
            .value_counts()
            .reindex(
                ["High", "Moderate", "Low"],
                fill_value=0,
            )
        )

        maximum = int(workload_counts.max())

        for label, value in workload_counts.items():
            render_bar(
                label,
                f"{int(value):,}",
                maximum if maximum else 1,
            )


# =========================================================
# DEPARTMENT TAB
# =========================================================

with tab_department:

    st.subheader("Department comparison")

    department_summary = (
        filtered
        .groupby("department", as_index=False)
        .agg(
            employees=("employee_id", "nunique"),
            attendance_rate=("attendance_rate", "mean"),
            performance_score=("performance_score", "mean"),
            late_count=("late_count", "mean"),
            absent_days=("absent_days", "mean"),
            target_achievement=("target_achievement", "mean"),
        )
    )

    numeric_columns = [
        "attendance_rate",
        "performance_score",
        "late_count",
        "absent_days",
        "target_achievement",
    ]

    department_summary[numeric_columns] = (
        department_summary[numeric_columns].round(2)
    )

    st.dataframe(
        department_summary,
        use_container_width=True,
        hide_index=True,
        height=330,
    )

    st.subheader("Average performance by department")

    performance_by_department = (
        department_summary
        .sort_values("performance_score", ascending=False)
    )

    maximum = float(
        performance_by_department["performance_score"].max()
    )

    for _, row in performance_by_department.iterrows():
        render_bar(
            row["department"],
            f'{row["performance_score"]:.1f}',
            maximum,
        )


# =========================================================
# RELATIONSHIP TAB
# =========================================================

with tab_relationship:

    st.subheader("Attendance and performance")

    st.caption(
        "This view explores association only. "
        "A correlation does not by itself show that attendance causes performance."
    )

    relation_left, relation_right = st.columns([1, 1.4])

    with relation_left:

        st.metric(
            "Correlation",
            f"{correlation:.2f}",
        )

        if correlation >= 0.5:
            interpretation = (
                "The sample shows a moderately strong positive relationship."
            )
        elif correlation >= 0.2:
            interpretation = (
                "The sample shows a mild positive relationship."
            )
        elif correlation <= -0.2:
            interpretation = (
                "The sample shows a negative relationship."
            )
        else:
            interpretation = (
                "The sample shows only a weak linear relationship."
            )

        st.info(interpretation)

        st.write(
            "Other factors such as workload, role differences, "
            "targets, and work complexity may also relate to performance."
        )

    with relation_right:

        scatter_data = (
            filtered[
                [
                    "attendance_rate",
                    "performance_score",
                ]
            ]
            .dropna()
        )

        st.scatter_chart(
            scatter_data,
            x="attendance_rate",
            y="performance_score",
            use_container_width=True,
        )


# =========================================================
# ATTENTION TAB
# =========================================================

with tab_attention:

    st.subheader("Employees that may need attention")

    employee_summary = (
        filtered
        .groupby(
            [
                "employee_id",
                "employee_name",
                "department",
            ],
            as_index=False,
        )
        .agg(
            attendance_rate=("attendance_rate", "mean"),
            performance_score=("performance_score", "mean"),
            late_count=("late_count", "sum"),
            absent_days=("absent_days", "sum"),
            target_achievement=("target_achievement", "mean"),
        )
    )

    employee_summary[
        "attention_flag"
    ] = (
        (employee_summary["attendance_rate"] < 90)
        |
        (employee_summary["performance_score"] < 75)
        |
        (employee_summary["late_count"] >= 12)
        |
        (employee_summary["absent_days"] >= 5)
    )

    attention = (
        employee_summary[
            employee_summary["attention_flag"]
        ]
        .copy()
    )

    attention[
        [
            "attendance_rate",
            "performance_score",
            "target_achievement",
        ]
    ] = (
        attention[
            [
                "attendance_rate",
                "performance_score",
                "target_achievement",
            ]
        ].round(2)
    )

    sort_option = st.selectbox(
        "Sort attention list by",
        [
            "Lowest performance",
            "Lowest attendance",
            "Most late occurrences",
            "Most absence days",
        ],
    )

    if sort_option == "Lowest performance":
        attention = attention.sort_values(
            "performance_score",
            ascending=True,
        )
    elif sort_option == "Lowest attendance":
        attention = attention.sort_values(
            "attendance_rate",
            ascending=True,
        )
    elif sort_option == "Most late occurrences":
        attention = attention.sort_values(
            "late_count",
            ascending=False,
        )
    else:
        attention = attention.sort_values(
            "absent_days",
            ascending=False,
        )

    st.dataframe(
        attention[
            [
                "employee_id",
                "employee_name",
                "department",
                "attendance_rate",
                "performance_score",
                "late_count",
                "absent_days",
                "target_achievement",
            ]
        ],
        use_container_width=True,
        hide_index=True,
        height=480,
    )

    st.caption(
        "Flags are simplified portfolio rules for prioritizing review, "
        "not formal HR evaluation criteria."
    )


# =========================================================
# DATA TAB
# =========================================================

with tab_data:

    st.subheader("Filtered employee records")

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True,
        height=520,
    )

    csv_data = (
        filtered
        .to_csv(index=False)
        .encode("utf-8-sig")
    )

    st.download_button(
        "Download filtered data",
        data=csv_data,
        file_name="attendance_performance_filtered.csv",
        mime="text/csv",
        use_container_width=True,
    )


# =========================================================
# FOOTER
# =========================================================

st.write("")
st.caption(
    "Portfolio project using synthetic employee attendance and performance data."
)
