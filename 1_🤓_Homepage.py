import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am JD Yang :wave:")
    st.title("A Senior Project Manager")
    st.write(
        """My major role is planning, developing, and executing projects in an organization. 
        I am also responsible for managing team members, compiling reports, cross-team coordination, 
        and other executive-level tasks."""
    )
    # st.write("[Learn More >](https://www.skinnovation.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On E&P projects, below are my responsibilities as Senior Manager in the position:  
            - Manage and coordinate multiple projects to ensure they are completed on time and on budget.
            - Communicate project status to management and key project participants.
            - Stay aware of company goals and strategies to ensure projects align with business priorities.
            - Facilitate and encourage collaboration across departments to ensure projects are completed successfully.
            - Optimize project deliverables, schedule, and budgeting.
            - Create presentations and reports to communicate project status.

            """
        )

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
