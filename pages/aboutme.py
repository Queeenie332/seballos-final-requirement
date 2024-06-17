import streamlit as st

def show_about_me():
    st.markdown("# ABOUT ME")
    st.markdown("""
 I am an extrovert with a passion for the arts, thriving on engaging with others and expressing my creativity in vibrant, dynamic ways. My outgoing personality and artistic talents make me the life of any gathering, always ready to inspire and energize those around me.
    """)

    st.markdown("---")

    st.image("pages/about_me_image.jpg")
    st.markdown("""
    Photo by [Your Name](https://example.com) on [Unsplash](https://unsplash.com)
    """)

    st.markdown("---")

    with st.expander("More about me"):
        st.markdown("""
       My journey in a BSIS course has been both challenging and rewarding, as I navigate the complexities of information systems and strive to master the integration of technology and business. Despite the tough demands of the coursework, the sense of accomplishment and joy I feel with each milestone makes the experience incredibly fulfilling.
        
        ### Personal Interests

        - **Taekwondo**: I love practicing Taekwondo; it's exhilarating.
        - **Reading Books and Novels**:Reading books and novels inspires me.
        - **Arts and Drawing**: Arts and drawing unleash my creativity.
        
        ### Future Goals

        In the next 5 years, I aim to excel in my BSIS career, achieve a black belt in Taekwondo, and continue enriching my life through reading and artistic endeavors.
        """)

    st.markdown("---")

    st.info("Connect with me on [Facebook](https://web.facebook.com/queenie.seballos)")
    st.info("Visit my personal website [here](https://web.facebook.com/queenie.seballos)")

# Main function to run the app
def main():
    show_about_me()

if __name__ == "__main__":
    main()
