import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "ITEQMT Machine Learning Application Portfolio", "💻"),
        Section("Machine Learning UI App", "🧙‍♂️"),
        Page("pages/aboutme.py", "ABOUT QUEENIE LYNN SEBALLOS", "1️⃣", in_section=True),
        Page("pages/discription.py", "APP DESCRIPTION", "2️⃣", in_section=True),
        Page("pages/learnings.py", "WHAT I HAVE LEARN?", "3️⃣", in_section=True),
    
  
        Section("PROJECTS", "💾"),
        Page("pages/predict.py", "PREDICTION", "1️⃣", in_section=True),
        Page("pages/sentiment.py", "SENTIMENT ANALYZER", "2️⃣", in_section=True),
        Page("pages/image.py", "IMAGE CLASSIFICATION", "3️⃣", in_section=True),


         Section("SOURCE CODE", "💾"),
        Page("pages/predict_src.py", "PREDICTION", "1️⃣", in_section=True),
        Page("pages/sentiment_src.py", "SENTIMENT ANALYZER", "2️⃣", in_section=True),
        Page("pages/image_src.py", "IMAGE CLASSIFICATION", "3️⃣", in_section=True),
    

    ]
)

hide_pages(["Thank you"])

st.markdown("### 👨‍🔧 ML Learning by [Queenie Lynn Seballos](https://github.com/Queeenie332/seballos-final-requirement)")

st.image("./p1.jpg")
st.markdown("""<a href="/photographer/thinkstock-83786">Thinkstock</a> on <a href="/">Freeimages.com</a>""",unsafe_allow_html=True,)

st.info("Visit the project [Github](https://github.com/Queeenie332/seballos-final-requirement)")
st.info("👨‍🔧 Please take note when on streamlit.app the [Image Classification] pages are not working due to Memory Limitation of 'Free Tier' hosting of Streamlit") 
st.markdown("---")

with st.expander("Sample ""st.expander"""):
    st.markdown("""
    
    <a href=""><img src="https://user-images.githubusercontent.com/875246/185755203-17945fd1-6b64-46f2-8377-1011dcb1a444.png" height="50" /></a>

    #

        HISTORY, PURPOSE AND USAGE
      
        In my Machine Learning Application Portfolio, I present a variety of innovative tools designed to address diverse challenges using advanced machine learning techniques. The Mushroom Datasets (Binary Classification) Model automates the classification of mushrooms based on characteristics, employing robust classification algorithms and data preprocessing methods. This application not only enhances accuracy in identifying edible and poisonous mushrooms but also supports ecological research, fungal species identification, and public safety by providing reliable mushroom classification capabilities.

        The Sentiment Analysis Tool meets the increasing demand for automated sentiment analysis in textual data. Utilizing natural language processing and machine learning advancements, this tool analyzes sentiment in text inputs to extract insights into customer feedback, social media sentiment, and communication patterns. Its goal is to streamline sentiment analysis across various applications, aiding decision-making and deepening understanding of textual data dynamics.

        The Crop Recommendation Predictor is essential for farmers seeking optimal crop choices based on soil nutrient levels. Developed with insights from precision agriculture and sustainable farming practices, this application recommends suitable crops by analyzing nitrogen, phosphorus, and potassium inputs. It helps farmers maximize crop yield and manage resources efficiently, promoting sustainable agricultural practices and enhancing productivity.

        In the realm of creative applications, the Image Style Transfer tool utilizes neural style transfer techniques to blend artistic styles between images. Leveraging advancements in computer vision and deep learning, this tool enables users to create visually striking compositions by merging the style of one image with the content of another. It empowers artists, photographers, and digital creators to explore new avenues of creativity in visual media and digital artistry.

        Finally, the Disease Diagnosis from Medical Images application revolutionizes medical diagnostics by automating disease detection and classification from medical imaging data. Built on convolutional neural networks (CNNs) and annotated medical datasets, this tool assists healthcare professionals in accurately identifying diseases from X-rays and MRIs. It aims to improve diagnostic precision, expedite treatment planning, and enhance patient outcomes through advanced machine learning technologies.

        In summary, each application in my portfolio embodies innovation, practicality, and significant impact across diverse domains. From agriculture and healthcare to digital art and sentiment analysis, these tools demonstrate the transformative potential of machine learning in addressing real-world challenges. By leveraging cutting-edge technologies and research, these applications contribute to smarter decision-making, enhanced automation, and creative expression, driving progress in their respective fields and shaping a more connected and intelligent future.

    #""", unsafe_allow_html=True)

st.markdown("""
### 👨‍🎓 Sample Header Title

##### 👨‍👦‍👦 Subheader Title

* Crop Prediction
* Sentiment Analyzer    
* Image Classification


##### 👨‍🔧 More Content

   HISTORY, PURPOSE AND USAGE
      In my Machine Learning Application Portfolio, I showcase a collection of innovative tools designed to tackle diverse challenges using advanced machine learning techniques. The Fruits Classification Model was created to automate fruit identification in images, employing state-of-the-art image processing and classification algorithms. This tool not only improves efficiency in fruit categorization but also aids agricultural research, inventory management, and consumer applications by delivering precise and automated fruit recognition capabilities.

The Sentiment Analysis Tool addresses the growing demand for automated sentiment analysis in textual data. Utilizing advancements in natural language processing and machine learning, this tool analyzes emotional content in text inputs to extract insights into customer feedback, social media sentiment, and communication patterns. Its objective is to streamline sentiment analysis processes across various domains, facilitating decision-making and deepening comprehension of textual data dynamics.

The Crop Recommendation Predictor is an essential resource for farmers aiming to optimize crop selection based on soil nutrient levels. Developed with insights from precision agriculture and sustainable farming practices, this application recommends suitable crops by analyzing nitrogen, phosphorus, and potassium inputs. It supports farmers in maximizing crop yield and resource management, thereby promoting sustainable agricultural practices and enhancing productivity.

In the realm of creative applications, the Image Style Transfer tool utilizes neural style transfer techniques to blend artistic styles between images. Drawing inspiration from advancements in computer vision and deep learning, this tool enables users to create visually compelling compositions by transferring the style of one image onto the content of another. It empowers artists, photographers, and digital creators to explore new dimensions of creativity in visual media and digital artistry.

Finally, the Disease Diagnosis from Medical Images application revolutionizes medical diagnostics by automating disease detection and classification from medical imaging data. Built on convolutional neural networks (CNNs) and annotated medical datasets, this tool assists healthcare professionals in making informed decisions by accurately identifying diseases from X-rays and MRIs. Its goal is to enhance diagnostic accuracy, expedite treatment planning, and improve patient outcomes through advanced machine learning technologies.

In conclusion, each application in my portfolio embodies innovation, practicality, and significant impact across diverse domains. From agriculture and healthcare to digital art and sentiment analysis, these tools showcase the transformative potential of machine learning in addressing real-world challenges. By leveraging cutting-edge technologies and rigorous research, these applications contribute to smarter decision-making, enhanced automation, and creative expression, paving the way for a more interconnected and intelligent future.

### 🔎 Overview""", unsafe_allow_html=True)


st.image("./p1.jpg")


st.markdown("""
    In my Machine Learning Application Portfolio, I showcase a diverse array of applications aimed at tackling real-world challenges through advanced machine learning techniques. A standout example is the Mushroom Dataset (Binary Classification) Model, utilizing image processing and classification algorithms to accurately discern between different types of mushrooms from uploaded images. Users can interactively upload images via a sidebar uploader, view predictions alongside the uploaded image, and explore the application's capabilities in real-time.

Another notable tool is the Sentiment Analysis Tool, designed to analyze the emotional tone of input sentences. This application employs a Naive Bayes classifier trained on labeled emotional expressions, providing immediate feedback on predicted emotions such as happiness, sadness, anger, excitement, nervousness, and fear. It offers a straightforward yet effective method for evaluating sentiment in text, enhancing communication analysis and processing customer feedback.

For agricultural applications, the Crop Recommendation Predictor assists farmers in making informed decisions by recommending suitable crops based on soil nutrient levels. Using a pre-trained Naive Bayes classifier loaded from a pickle file, this tool adjusts sliders for nitrogen, phosphorus, and potassium inputs to predict the best crop match. It serves as a valuable resource for optimizing crop yield and ensuring sustainable farming practices.

Additionally, the Image Style Transfer application enables creative transformations of visual content by merging artistic styles from one image onto the content of another. Users upload two images—one for content and another for style—and adjust style transfer parameters to achieve unique artistic effects. This application leverages machine learning to blend artistic creativity with digital imagery.

Lastly, the Disease Diagnosis from Medical Images tool aids medical diagnostics by analyzing medical images such as X-rays or MRIs to detect and classify diseases. Using convolutional neural networks (CNNs) trained on annotated medical datasets, this application provides accurate diagnoses and visual feedback on detected diseases. It supports healthcare professionals in making informed decisions and improving patient care outcomes.

In conclusion, each application in my portfolio showcases the practical application of machine learning across diverse domains, including agriculture, healthcare, creative arts, and communication analysis. These tools exemplify the versatility and impact of machine learning in enhancing decision-making, automation, and creativity, catering to various user needs and driving innovation in their respective fields.
            
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
