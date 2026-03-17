import streamlit as st
import pandas as pd
import mysql.connector

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aravinth@2431",
    database="uber_data"
)

# Page Selection (NO SIDEBAR CONFUSION)
page = st.selectbox("Select Page", ["Dashboard", "Q&A"])

# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    st.title("📊 Uber Restaurant Dashboard")

    option = st.selectbox(
        "Choose Analysis",
        ("Restaurant Type", "Online Order", "Table Booking")
    )

    query = ""

    if option == "Restaurant Type":
        query = "SELECT rest_type, COUNT(*) as count FROM uber_ak GROUP BY rest_type"

    elif option == "Online Order":
        query = "SELECT online_order, COUNT(*) as count FROM uber_ak GROUP BY online_order"

    elif option == "Table Booking":
        query = "SELECT book_table, COUNT(*) as count FROM uber_ak GROUP BY book_table"

    df = pd.read_sql(query, conn)
    st.dataframe(df)

# ---------------- Q&A ----------------
elif page == "Q&A":

    st.title("❓ Business Questions")

    question = st.selectbox(
        "Select Question",
        (
            "Top locations by rating",
            "Most restaurants by location",
            "Online order impact",
            "Table booking impact",
            "Cost vs rating",
            "Top restaurants by rating",
            "Top restaurants by votes",
            "Most common cuisines",
            "Highest rated cuisines",
            "Location cost vs rating",
            "Best locations for premium restaurants",
            "Locations with low rating",
            "Restaurants with online & table booking",
            "Top cost restaurants",
            "Low cost high rating restaurants"
        )
    )

    query = ""

    if question == "Top locations by rating":
        query = "SELECT location, AVG(rate) as avg_rating FROM uber_ak GROUP BY location ORDER BY avg_rating DESC"

    elif question == "Most restaurants by location":
        query = "SELECT location, COUNT(*) as count FROM uber_ak GROUP BY location ORDER BY count DESC"

    elif question == "Online order impact":
        query = "SELECT online_order, AVG(rate) as avg_rating FROM uber_ak GROUP BY online_order"

    elif question == "Table booking impact":
        query = "SELECT book_table, AVG(rate) as avg_rating FROM uber_ak GROUP BY book_table"

    elif question == "Cost vs rating":
        query = "SELECT approx_cost, AVG(rate) as avg_rating FROM uber_ak GROUP BY approx_cost"

    elif question == "Top restaurants by rating":
        query = "SELECT name, rate FROM uber_ak ORDER BY rate DESC LIMIT 10"

    elif question == "Top restaurants by votes":
        query = "SELECT name, votes FROM uber_ak ORDER BY votes DESC LIMIT 10"

    elif question == "Most common cuisines":
        query = "SELECT cuisines, COUNT(*) as count FROM uber_ak GROUP BY cuisines ORDER BY count DESC LIMIT 10"

    elif question == "Highest rated cuisines":
        query = "SELECT cuisines, AVG(rate) as avg_rating FROM uber_ak GROUP BY cuisines ORDER BY avg_rating DESC LIMIT 10"

    elif question == "Location cost vs rating":
        query = "SELECT location, AVG(approx_cost) as avg_cost, AVG(rate) as avg_rating FROM uber_ak GROUP BY location"

    elif question == "Best locations for premium restaurants":
        query = "SELECT location, AVG(rate) as rating, AVG(approx_cost) as cost FROM uber_ak GROUP BY location ORDER BY rating DESC"

    elif question == "Locations with low rating":
        query = "SELECT location, AVG(rate) as rating FROM uber_ak GROUP BY location ORDER BY rating ASC"

    elif question == "Restaurants with online & table booking":
        query = "SELECT name, rate FROM uber_ak WHERE online_order='Yes' AND book_table='Yes' ORDER BY rate DESC"

    elif question == "Top cost restaurants":
        query = "SELECT name, approx_cost FROM uber_ak ORDER BY approx_cost DESC LIMIT 10"

    elif question == "Low cost high rating restaurants":
        query = "SELECT name, approx_cost, rate FROM uber_ak ORDER BY rate DESC LIMIT 10"

    df = pd.read_sql(query, conn)
    st.dataframe(df)