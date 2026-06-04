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
# LOAD DATA
# --------------------------------

stock_df = pd.read_csv("data/RELIANCE_ANALYZED.csv")
news_df = pd.read_csv("data/reliance_news_sentiment.csv")
impact_df = pd.read_csv("data/advanced_impact_dataset.csv")

# --------------------------------
# SIDEBAR
# --------------------------------

st.sidebar.title("📈 Stock Event Analyzer")

st.sidebar.markdown("""
Analyze how stock prices react to
financial news using AI-powered
sentiment analysis.
""")

# --------------------------------
# TITLE
# --------------------------------

st.title("📈 Stock Event Analyzer")
st.markdown("### Reliance Industries News & Stock Impact Dashboard")

st.divider()

# --------------------------------
# METRICS
# --------------------------------

positive_count = len(news_df[news_df["label"] == "positive"])
negative_count = len(news_df[news_df["label"] == "negative"])
neutral_count = len(news_df[news_df["label"] == "neutral"])

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

st.header("📊 Reliance Stock Price")

stock_df["Date"] = pd.to_datetime(stock_df["Date"])

stock_chart = px.line(
    stock_df,
    x="Date",
    y="Close",
    title="Reliance Closing Price"
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

    st.header("📉 Average Next-Day Return by Sentiment")

    sentiment_returns = (
        impact_df
        .groupby("sentiment")["next_day_return"]
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
# FOOTER
# --------------------------------

st.divider()

st.markdown(
    """
    Built using:
    - Yahoo Finance
    - News API
    - FinBERT
    - Pandas
    - Streamlit
    - Plotly
    """
)