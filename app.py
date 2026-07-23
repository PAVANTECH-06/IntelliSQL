import streamlit as st
import google.generativeai as genai
import sqlite3
import os
from dotenv import load_dotenv
import pandas as pd
import plotly.express as px
from datetime import datetime
import time

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="IntelliSQL",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# SESSION STATE
# ==========================

if "history" not in st.session_state:
    st.session_state.history = []

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2103/2103633.png",
        width=90
    )

    st.title("IntelliSQL")

    st.markdown("---")

    st.session_state.theme = st.radio(
        "🎨 Theme",
        ["Dark", "Light"],
        horizontal=True
    )

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "ℹ️ About",
            "🧠 Intelligent Query Assistant"
        ]
    )

    st.markdown("---")

    st.subheader("Project")

    st.success("Google Gemini AI")

    st.info("SQLite Database")

    st.warning("Natural Language → SQL")

    st.markdown("---")

    st.caption("Version 2.0")

# ==========================
# COLOR PALETTE
# ==========================

if st.session_state.theme == "Dark":

    BG = "#0F172A"
    CARD = "#1E293B"
    SIDEBAR = "#111827"
    TEXT = "#F8FAFC"
    PRIMARY = "#3B82F6"
    SECONDARY = "#8B5CF6"

else:

    BG = "#F8FAFC"
    CARD = "#FFFFFF"
    SIDEBAR = "#E2E8F0"
    TEXT = "#111827"
    PRIMARY = "#2563EB"
    SECONDARY = "#7C3AED"

# ==========================
# CUSTOM CSS
# ==========================

st.markdown(
    f"""
<style>

.stApp{{
background:{BG};
color:{TEXT};
}}

section[data-testid="stSidebar"]{{
background:{SIDEBAR};
}}

.block-container{{
padding-top:2rem;
padding-bottom:2rem;
}}

h1,h2,h3,h4,h5{{
color:{PRIMARY};
font-weight:700;
}}

.card{{
background:{CARD};
padding:25px;
border-radius:18px;
box-shadow:0 8px 25px rgba(0,0,0,.25);
margin-bottom:18px;
transition:.3s;
}}

.card:hover{{
transform:translateY(-6px);
}}

.hero{{
background:linear-gradient(
135deg,
{PRIMARY},
{SECONDARY}
);
padding:40px;
border-radius:20px;
color:white;
text-align:center;
margin-bottom:25px;
}}

.metric-card{{
background:{CARD};
padding:20px;
border-radius:15px;
text-align:center;
box-shadow:0 4px 15px rgba(0,0,0,.18);
}}

.feature{{
background:{CARD};
padding:20px;
border-left:6px solid {PRIMARY};
border-radius:15px;
margin-bottom:15px;
box-shadow:0 6px 15px rgba(0,0,0,.2);
}}

.stButton>button{{
width:100%;
height:55px;
font-size:18px;
font-weight:bold;
border:none;
border-radius:14px;
background:linear-gradient(
90deg,
{PRIMARY},
{SECONDARY}
);
color:white;
transition:.3s;
}}

.stButton>button:hover{{
transform:scale(1.02);
box-shadow:0 10px 25px rgba(59,130,246,.45);
}}

.sql-box{{
background:#111827;
padding:20px;
border-radius:15px;
color:#22C55E;
font-family:monospace;
font-size:16px;
}}

.footer{{
text-align:center;
margin-top:50px;
padding:20px;
opacity:.8;
}}

</style>
""",
    unsafe_allow_html=True,
)

# ==========================
# LOAD GEMINI
# ==========================

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# ==========================
# DATABASE
# ==========================

DATABASE = "database.db"

def execute_query(sql):

    conn = sqlite3.connect(DATABASE)

    try:

        df = pd.read_sql_query(sql, conn)

        conn.close()

        return df

    except Exception as e:

        conn.close()

        return str(e)


def generate_sql(question):

    prompt = f"""
You are an SQLite Expert.

Convert the user question into a valid SQLite query.

Schema:

customers(
id,
name,
city
)

orders(
order_id,
customer_id,
product,
amount
)

Rules

Only SELECT queries.

Never UPDATE

Never DELETE

Never DROP

Never INSERT

Return ONLY SQL.

Question:

{question}

"""

    response = model.generate_content(prompt)

    sql = response.text.strip()

    sql = sql.replace("```sql", "")

    sql = sql.replace("```", "")

    return sql.strip()


def explain_sql(sql):

    prompt = f"""
Explain this SQL query in simple English.

{sql}

Explain in bullet points.
"""

    response = model.generate_content(prompt)

    return response.text

# ==========================
# HOME PAGE
# ==========================

if page == "🏠 Home":

    st.markdown(
        f"""
<div class="hero">

<h1>🤖 IntelliSQL</h1>

<h3>
AI Powered Natural Language Database Assistant
</h3>

<p>
Transform English into Optimized SQL using Google Gemini AI
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            """
<div class="metric-card">

<h2>🤖</h2>

<h3>Gemini AI</h3>

<p>LLM Engine</p>

</div>
""",
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
<div class="metric-card">

<h2>🗄️</h2>

<h3>SQLite</h3>

<p>Database</p>

</div>
""",
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            """
<div class="metric-card">

<h2>⚡</h2>

<h3>Fast</h3>

<p>Query Generation</p>

</div>
""",
            unsafe_allow_html=True,
        )

    with c4:
        st.markdown(
            """
<div class="metric-card">

<h2>🔒</h2>

<h3>Secure</h3>

<p>Read Only</p>

</div>
""",
            unsafe_allow_html=True,
        )
    st.markdown("<br>", unsafe_allow_html=True)

    left, right = st.columns([1, 1])

    with left:

        st.markdown("""
<div class="feature">

<h3>💡 Intelligent Query Assistance</h3>

<p>
Ask database questions in plain English and let Gemini generate optimized SQL automatically.
</p>

</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="feature">

<h3>📊 Data Exploration</h3>

<p>
Retrieve structured information quickly without writing SQL manually.
</p>

</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="feature">

<h3>⚡ Performance Optimized</h3>

<p>
Uses prompt engineering to generate clean SQLite queries.
</p>

</div>
""", unsafe_allow_html=True)

    with right:

        st.markdown("""
<div class="feature">

<h3>🔒 Secure Execution</h3>

<p>
Only SELECT statements are executed.
Dangerous SQL commands are blocked.
</p>

</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="feature">

<h3>🧠 Gemini Powered</h3>

<p>
Built using Google's latest Gemini Large Language Model.
</p>

</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="feature">

<h3>📈 Interactive Results</h3>

<p>
Visualize returned data instantly using charts and tables.
</p>

</div>
""", unsafe_allow_html=True)

# ===================================
# ABOUT PAGE
# ===================================

elif page == "ℹ️ About":

    st.title("ℹ️ About IntelliSQL")

    st.markdown("""
<div class="card">

## 🚀 Project Overview

IntelliSQL is an AI-powered SQL Assistant that allows users to interact
with databases using natural language.

Instead of writing SQL manually,
users simply ask questions in English.

Google Gemini converts the question
into optimized SQLite queries and retrieves the results instantly.

</div>
""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:

        st.subheader("✨ Features")

        st.success("Natural Language → SQL")

        st.success("Gemini AI Integration")

        st.success("SQLite Support")

        st.success("Automatic SQL Generation")

        st.success("Interactive Data Tables")

        st.success("Query Explanation")

        st.success("CSV Download")

        st.success("Charts")

    with c2:

        st.subheader("🛠 Tech Stack")

        tech = pd.DataFrame(
            {
                "Technology": [
                    "Python",
                    "Streamlit",
                    "Google Gemini",
                    "SQLite",
                    "Pandas",
                    "Plotly"
                ],
                "Purpose": [
                    "Backend",
                    "Frontend",
                    "LLM",
                    "Database",
                    "Data Processing",
                    "Visualization"
                ]
            }
        )

        st.dataframe(
            tech,
            use_container_width=True,
            hide_index=True
        )

    st.markdown("---")

    st.subheader("📌 Workflow")

    st.markdown("""

1. User asks a question.

2. Gemini converts it into SQL.

3. SQL executes on SQLite.

4. Results displayed instantly.

5. User can visualize and download.

""")

# ===================================
# QUERY PAGE
# ===================================

elif page == "🧠 Intelligent Query Assistant":

    st.title("🧠 Intelligent Query Assistant")

    st.caption("Ask anything about your database.")

    st.sidebar.subheader("Database Schema")

    st.sidebar.code("""
customers
---------
id
name
city

orders
---------
order_id
customer_id
product
amount
""")

    question = st.text_area(
        "💬 Enter your question",
        placeholder="Example: Show all customers from Hyderabad"
    )

    col1, col2 = st.columns([3,1])

    with col1:

        generate = st.button(
            "🚀 Generate & Execute"
        )

    with col2:

        clear = st.button(
            "🗑 Clear History"
        )

    if clear:

        st.session_state.history = []

        st.success("History Cleared")

    if generate:

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            with st.spinner("Gemini is generating SQL..."):

                time.sleep(1)

                sql = generate_sql(question)

            st.subheader("📝 Generated SQL")

            st.code(
                sql,
                language="sql",
                line_numbers=True
            )
            sql= sql.strip()

            if not sql.lower().startswith("select"):

                st.error("Only SELECT queries are allowed.")
                st.stop()

            else:

                result = execute_query(sql)

                st.session_state.history.append(
                    {
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "question": question,
                        "sql": sql
                    }
                )
		                # ------------------------------
                # QUERY EXECUTION RESULT
                # ------------------------------

                if isinstance(result, pd.DataFrame):
                    if result.empty:
                         st.warning("No records found.")
                         st.stop()

                    st.success(
                        f"✅ Query executed successfully. {len(result)} row(s) returned."
                    )

                    st.subheader("📊 Query Results")

                    st.dataframe(
                        result,
                        use_container_width=True,
                        hide_index=True
                    )

                    # --------------------------
                    # DOWNLOAD CSV
                    # --------------------------

                    csv = result.to_csv(index=False).encode("utf-8")

                    st.download_button(
                        label="📥 Download CSV",
                        data=csv,
                        file_name="query_results.csv",
                        mime="text/csv"
                    )

                    # --------------------------
                    # AUTO VISUALIZATION
                    # --------------------------

                    if len(result.columns) >= 2:

                        st.subheader("📈 Data Visualization")

                        numeric_columns = result.select_dtypes(
                            include=["number"]
                        ).columns.tolist()

                        if numeric_columns:

                            x_axis = st.selectbox(
                                "Select X-axis",
                                result.columns,
                                key="x_axis"
                            )

                            y_axis = st.selectbox(
                                "Select Y-axis",
                                numeric_columns,
                                key="y_axis"
                            )

                            chart_type = st.selectbox(
                                "Chart Type",
                                [
                                    "Bar",
                                    "Line",
                                    "Pie",
                                    "Scatter"
                                ]
                            )

                            if chart_type == "Bar":

                                fig = px.bar(
                                    result,
                                    x=x_axis,
                                    y=y_axis,
                                    title="Bar Chart"
                                )

                            elif chart_type == "Line":

                                fig = px.line(
                                    result,
                                    x=x_axis,
                                    y=y_axis,
                                    title="Line Chart"
                                )

                            elif chart_type == "Pie":

                                fig = px.pie(
                                    result,
                                    names=x_axis,
                                    values=y_axis,
                                    title="Pie Chart"
                                )

                            else:

                                fig = px.scatter(
                                    result,
                                    x=x_axis,
                                    y=y_axis,
                                    title="Scatter Plot"
                                )

                            st.plotly_chart(
                                fig,
                                use_container_width=True
                            )

                    # --------------------------
                    # SQL EXPLANATION
                    # --------------------------

                    with st.expander(
                        "🧠 Explain Generated SQL"
                    ):

                        with st.spinner(
                            "Generating explanation..."
                        ):

                            explanation = explain_sql(sql)

                        st.markdown(explanation)

                else:

                    st.error(result)

    # ------------------------------------------
    # QUERY HISTORY
    # ------------------------------------------

    if st.session_state.history:

        st.markdown("---")

        st.subheader("🕒 Recent Queries")

        for item in reversed(st.session_state.history):

            with st.expander(
                f"{item['time']}  |  {item['question']}"
            ):

                st.code(
                    item["sql"],
                    language="sql"
                )

# ======================================
# FOOTER
# ======================================

st.markdown(
    """
<hr>

<div class="footer">

<h4>🤖 IntelliSQL</h4>

<p>
Built with ❤️ using
Python • Streamlit • Google Gemini • SQLite • Plotly
</p>

<p>
AI Powered Natural Language Database Assistant
</p>

</div>

""",
    unsafe_allow_html=True,
)
