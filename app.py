import streamlit as st
import json
import yaml
from pathlib import Path
import sys

# Load data
def load_data():
    # Adjust these paths depending on your directory structure
    categories = yaml.load(open("./lib/categories.yaml", "r"), Loader=yaml.FullLoader)

    with open('./lib/data.json') as f:
        data = json.load(f)
    data = sorted(data, key=lambda x: x["coverage_score"], reverse=True)

    return categories, data


# Streamlit app
def app():
    categories, data = load_data()

    st.title("concurrent.news")
    st.header("June 2, 2023")

    # Category filter
    category = st.selectbox("Choose a category", ["All"] + categories)

    # Display data
    for item in data:
        if category == "All" or item["category"] == category:
            with st.expander(item["banner"], expanded=False):
                st.text(item["title"])
                st.text(item["summary"])
                # st.text(item["detail"])

                st.write("Sources:")
                for subitem in item["source-articles"]:
                    st.write(f"- [{subitem['title']}]({subitem['url']})")


# Run the app
if __name__ == "__main__":
    app()
