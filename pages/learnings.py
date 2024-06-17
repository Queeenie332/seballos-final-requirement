import streamlit as st

def show_learnings():
    st.markdown("# WHAT I HAVE LEARNED")

    st.markdown("""    
    Creating these applications has been a fulfilling experience, enabling me to explore diverse facets of machine learning and data science. Here are key insights gained from each project:
    """)

    st.markdown("## Crop Prediction 🌾")
    st.markdown("""
    - **Data Visualization**: I've honed my skills in creating insightful visualizations that communicate complex trends and patterns in agricultural data.
    - **Predictive Analytics**: Applied classification algorithms to forecast pest outbreaks in crops, leveraging historical data and environmental factors.
    - **Research and Development**: Acquired insights into agricultural practices and the importance of data-driven decision-making in farming.
    """)

    st.markdown("## Sentiment Analyzer 😊")
    st.markdown("""
    - **Natural Language Processing (NLP)**: Explored NLP techniques for text preprocessing, feature extraction, and sentiment analysis using libraries like NLTK and spaCy.
    - **Model Evaluation**: Learned methods to evaluate sentiment analysis models, including accuracy metrics and handling sentiment polarity variations.
    - **Application in Business**: Conducted studies on emerging agricultural technologies, exploring their potential to revolutionize yield optimization and sustainable farming practices.
    """)

    st.markdown("## Image Classification 🖼️")
    st.markdown("""
    - **Natural Language Processing**: Explored advanced techniques in NLP using models such as BERT, GPT-3, and Transformer for tasks like sentiment analysis and language generation.
    - **Reinforcement Learning**:  Implemented RL algorithms like Deep Q-Networks (DQN) and Policy Gradient methods to solve complex decision-making problems in environments such as game simulations and robotics.
    - **Time Series Forecasting**: Applied LSTM and GRU networks to predict trends in financial markets, energy consumption, and weather patterns, demonstrating the versatility of neural networks in sequential data analysis.
    """)

    st.markdown("---")

    st.info("These projects have furnished me with practical expertise in machine learning, encompassing data preprocessing, model evaluation, and domain-specific insights.. Connect with me on [Facebook](https://web.facebook.com/queenie.seballos) to discuss more about these projects!")

# Main function to run the app
def main():
    show_learnings()

if __name__ == "__main__":
    main()
