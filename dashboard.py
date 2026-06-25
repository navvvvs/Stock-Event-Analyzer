import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="Stock Event Analyzer",
    page_icon="📈",
    layout="wide"
)

# --------------------------------
# SIDEBAR
# --------------------------------

st.sidebar.title("📈 Stock Event Analyzer")


company = st.sidebar.selectbox(
    "Select Company",
    [
        "RELIANCE",
        "TCS",
        "INFY",
        "HDFCBANK",
        "ICICIBANK",
        "SBIN",
        "WIPRO",
        "LT"
    ]
)

st.sidebar.markdown("""
Analyze how stock prices react to
financial news using AI-powered
sentiment analysis.
""")

# --------------------------------
# LOAD DATA
# --------------------------------

stock_df = pd.read_csv(
    f"data/{company}_ANALYZED.csv"
)

news_df = pd.read_csv(
    f"data/{company.lower()}_news_sentiment.csv"
)

impact_df = pd.read_csv(
    f"data/{company.lower()}_impact.csv"
)

# --------------------------------
# TITLE
# --------------------------------

st.title("📈 Stock Event Analyzer")

st.markdown(
    f"### {company} News & Stock Impact Dashboard"
)

st.divider()

# --------------------------------
# METRICS
# --------------------------------

positive_count = len(
    news_df[news_df["label"] == "positive"]
)

negative_count = len(
    news_df[news_df["label"] == "negative"]
)

neutral_count = len(
    news_df[news_df["label"] == "neutral"]
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "News Articles",
        len(news_df)
    )

with col2:
    st.metric(
        "Positive News",
        positive_count
    )

with col3:
    st.metric(
        "Negative News",
        negative_count
    )

with col4:
    st.metric(
        "Neutral News",
        neutral_count
    )

st.divider()

# --------------------------------
# STOCK PRICE CHART
# --------------------------------

st.header(f"📊 {company} Stock Price")

stock_df["Date"] = pd.to_datetime(
    stock_df["Date"]
)

stock_chart = px.line(
    stock_df,
    x="Date",
    y="Close",
    title=f"{company} Closing Price"
)

st.plotly_chart(
    stock_chart,
    use_container_width=True
)

# --------------------------------
# SENTIMENT DISTRIBUTION
# --------------------------------

st.header("📰 News Sentiment Distribution")

pie_chart = px.pie(
    news_df,
    names="label",
    title="Sentiment Breakdown"
)

st.plotly_chart(
    pie_chart,
    use_container_width=True
)

# --------------------------------
# LATEST NEWS
# --------------------------------

st.header("📰 Latest News")

st.dataframe(
    news_df[
        ["title", "label", "score"]
    ],
    use_container_width=True
)

# --------------------------------
# IMPACT DATASET
# --------------------------------

st.header("📈 News Impact Analysis")

st.dataframe(
    impact_df,
    use_container_width=True
)

# --------------------------------
# IMPACT BY SENTIMENT
# --------------------------------

if len(impact_df) > 0:

    st.header(
        "📉 Average Next-Day Return by Sentiment"
    )

    sentiment_returns = (
        impact_df
        .groupby("sentiment")[
            "next_day_return"
        ]
        .mean()
        .reset_index()
    )

    bar_chart = px.bar(
        sentiment_returns,
        x="sentiment",
        y="next_day_return",
        title="Average Return by Sentiment"
    )

    st.plotly_chart(
        bar_chart,
        use_container_width=True
    )

# --------------------------------
# COMPANY COMPARISON
# --------------------------------

st.header("📊 Company Comparison")

companies = [
    "RELIANCE",
    "TCS",
    "INFY",
    "HDFCBANK",
    "ICICIBANK",
    "SBIN",
    "WIPRO",
    "LT"
]

comparison_data = []

for comp in companies:

    news = pd.read_csv(
        f"data/{comp.lower()}_news_sentiment.csv"
    )

    impact = pd.read_csv(
        f"data/{comp.lower()}_impact.csv"
    )

    total_articles = len(news)

    positive_pct = (
        len(news[news["label"] == "positive"])
        / total_articles
    ) * 100

    negative_pct = (
        len(news[news["label"] == "negative"])
        / total_articles
    ) * 100

    avg_return = (
        impact["next_day_return"].mean()
        if len(impact) > 0
        else 0
    )

    comparison_data.append({
        "Company": comp,
        "Articles": total_articles,
        "Positive %": round(positive_pct, 2),
        "Negative %": round(negative_pct, 2),
        "Avg Next-Day Return %": round(avg_return, 2)
    })

comparison_df = pd.DataFrame(
    comparison_data
)

st.dataframe(
    comparison_df,
    use_container_width=True
)

st.subheader("📈 Average Return Comparison")

return_chart = px.bar(
    comparison_df,
    x="Company",
    y="Avg Next-Day Return %",
    title="Average Next-Day Return by Company"
)

st.plotly_chart(
    return_chart,
    use_container_width=True
)

st.subheader("😊 Positive Sentiment Comparison")

positive_chart = px.bar(
    comparison_df,
    x="Company",
    y="Positive %",
    title="Positive News Percentage by Company"
)

st.plotly_chart(
    positive_chart,
    use_container_width=True
)

# --------------------------------
# STOCK PERFORMANCE COMPARISON
# --------------------------------

st.header("📈 Stock Performance Comparison")

stock_list = []

for comp in companies:

    temp = pd.read_csv(
        f"data/{comp}_ANALYZED.csv"
    )

    temp["Date"] = pd.to_datetime(
        temp["Date"]
    )

    temp = temp[["Date", "Close"]]

    temp["Company"] = comp

    stock_list.append(temp)

comparison_stock = pd.concat(
    stock_list,
    ignore_index=True
)

stock_compare_chart = px.line(
    comparison_stock,
    x="Date",
    y="Close",
    color="Company",
    title="Stock Price Comparison"
)

st.plotly_chart(
    stock_compare_chart,
    use_container_width=True
)

# --------------------------------
# SENTIMENT VS RETURN ANALYSIS
# --------------------------------

st.header("🧠 Sentiment vs Stock Return Analysis")

all_impacts = []

for comp in companies:

    temp = pd.read_csv(
        f"data/{comp.lower()}_impact.csv"
    )

    temp["Company"] = comp

    all_impacts.append(temp)

combined_df = pd.concat(
    all_impacts,
    ignore_index=True
)

sentiment_analysis = (
    combined_df
    .groupby("sentiment")["next_day_return"]
    .mean()
    .reset_index()
)

st.dataframe(
    sentiment_analysis,
    use_container_width=True
)

correlation_chart = px.bar(
    sentiment_analysis,
    x="sentiment",
    y="next_day_return",
    title="Average Return by Sentiment"
)

st.plotly_chart(
    correlation_chart,
    use_container_width=True
)

# --------------------------------
# KEY INSIGHTS
# --------------------------------

st.header("💡 Key Insights")

best_company = comparison_df.loc[
    comparison_df["Avg Next-Day Return %"].idxmax()
]

most_positive = comparison_df.loc[
    comparison_df["Positive %"].idxmax()
]

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Best Performing Company",
        best_company["Company"],
        f"{best_company['Avg Next-Day Return %']}%"
    )

with col2:
    st.metric(
        "Most Positive News",
        most_positive["Company"],
        f"{most_positive['Positive %']}%"
    )

# --------------------------------
# FOOTER
# --------------------------------

st.divider()

st.markdown("""
Built using:

- Yahoo Finance
- NewsAPI
- FinBERT
- Pandas
- Streamlit
- Plotly
""")