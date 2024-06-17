import streamlit as st

def show_app_description():
    st.markdown("# APP DESCRIPTION")

    st.markdown("""
    Welcome to my Streamlit application portfolio. I exhibit three captivating projects that epitomize my proficiency and ardor for machine learning and data science.
    """)

    st.markdown("## Machine Learning Applications")

    st.markdown("### Crop Prediction 🌾")
    st.markdown("""
    This application employs sophisticated machine learning models to forecast crop yields by analyzing historical data, weather patterns, and soil conditions. Its objective is to aid farmers in making well-informed decisions for optimal crop planning and management.
    """)

    st.markdown("### Sentiment Analyzer 😊")
    st.markdown("""
    The sentiment analyzer utilizes natural language processing (NLP) techniques for analyzing and classifying text sentiment, aiding businesses in comprehending customer feedback, social media sentiment, and review sentiments to derive actionable insights.
    """)

    st.markdown("### Image Classification 🖼️")
    st.markdown("""
    This application utilizes deep learning models for classifying images into predefined categories, facilitating tasks like object identification, facial recognition, and medical image analysis. Dive into the capabilities of image recognition through this interactive tool.
    """)

    st.markdown("---")

    st.info("Explore each application to witness demonstrations and gain a deeper understanding of the underlying technology.")
    st.info("Connect with me on [Facebook](https://web.facebook.com/queenie.seballos) for collaborations and discussions.")

# Main function to run the app
def main():
    show_app_description()

if __name__ == "__main__":
    main()
