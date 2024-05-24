import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="REF - FIND", page_icon=":tada:", layout="wide")


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

# ---- LOAD ASSETS ----
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_coding = load_lottieurl("https://lottie.host/8db80b81-8dc5-433c-a70b-a97dec55e6cf/h8nedB3p76.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.title("Welcome to Ref-find:wave:")
    st.subheader("!!!WHISTLE IN HAND, GAME IN COMMAND!!!")
    st.write(
        "Ref-Find is a first of it's kind application that is created with the Assigner and official in mind.Designed to allow both the official and Agent to find the assignment that makes the most sense and is the most efficient. Ref find was developed by a team of current officials with over of 20 years of real life experience of scheduling and working in the field. Our application aims to more efficiently help both officials and agents work together to get games covered more quickly by using location services and matching officials with games."
    )
    #st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we provide")
        st.write("##")
        st.write(
            """
            With our app and association with the Referee Organiztion, we:
            - Streamlined Booking: Easily book referees for games and events with just a few clicks.
            - In-App Communication: Directly communicate with referees through the app for quick and efficient coordination.
            - User-Friendly Interface: Navigate the app with ease thanks to its intuitive and user-friendly design.
            - Community Building: Connect with a community of referees and sports organizers."

            If this sounds interesting to you, consider JOINING our locally made app, so we can make your schedule and games easier.
            """
        )
        #st.write("[Get App >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


with st.container():
    st.subheader("Privacy Policy")
    st.write(
        """
        Effective Date: May 23, 2024

        1. Introduction
        Welcome to Ref Find. We value your privacy and are committed to protecting your personal information. This Privacy Policy outlines
        how we collect, use, disclose, and safeguard your information when you visit our website [www.ref-find.com] (the "Site") and use our services. 
        By using our Site and services, you agree to the terms of this Privacy Policy.

        2. Information We Collect
        We may collect information about you in a variety of ways. The information we may collect on the Site includes:

        Personal Data
        While using our Site, we may ask you to provide us with certain personally identifiable information that can be used to contact or 
        identify you, including but not limited to: Name, Email address, Phone number, Address, Usage Data
        We may also collect information that your browser sends whenever you visit our Site or when you access the Site by or through a mobile device. 
        This Usage Data may include information such as:

        Your computer's Internet Protocol (IP) address
        Browser type
        Browser version
        The pages of our Site that you visit
        The time and date of your visit
        The time spent on those pages
        Unique device identifiers
        Other diagnostic data
        Cookies and Tracking Technologies
        We use cookies and similar tracking technologies to track the activity on our Site and hold certain information. Cookies are files with a 
        small amount of data that may include an anonymous unique identifier. You can instruct your browser to refuse all cookies or to indicate 
        when a cookie is being sent.

        3. How We Use Your Information
        We use the collected data for various purposes:

        To provide and maintain our Site and services
        To notify you about changes to our Site and services
        To allow you to participate in interactive features of our Site when you choose to do so
        To provide customer support
        To gather analysis or valuable information so that we can improve our Site
        To monitor the usage of our Site
        To detect, prevent, and address technical issues
        To fulfill any other purpose for which you provide it
        4. Sharing Your Information
        We do not sell, trade, or otherwise transfer to outside parties your Personally Identifiable Information unless we provide users with 
        advance notice. This does not include website hosting partners and other parties who assist us in operating our website, conducting our 
        business, or serving our users, so long as those parties agree to keep this information confidential.

        We may also release information when it's release is appropriate to comply with the law, enforce our site policies, or protect ours or 
        others' rights, property or safety.

        5. Security of Your Information
        We use administrative, technical, and physical security measures to help protect your personal information. While we have taken reasonable 
        steps to secure the personal information you provide to us, please be aware that despite our efforts, no security measures are perfect or 
        impenetrable, and no method of data transmission can be guaranteed against any interception or other type of misuse.

        6. Your Data Protection Rights
        Depending on your location, you may have the following rights regarding your personal data:

        The right to access  You have the right to request copies of your personal data.
        The right to rectification  You have the right to request that we correct any information you believe is inaccurate or incomplete.
        The right to erasure  You have the right to request that we erase your personal data, under certain conditions.
        The right to restrict processing  You have the right to request that we restrict the processing of your personal data, under certain 
        conditions.
        The right to object to processing  You have the right to object to our processing of your personal data, under certain conditions.
        The right to data portability  You have the right to request that we transfer the data that we have collected to another organization, 
        or directly to you, under certain conditions.
        If you make a request, we have one month to respond to you. If you would like to exercise any of these rights, please contact us at our 
        provided contact information.

        7. Changes to This Privacy Policy
        We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page. You 
        are advised to review this Privacy Policy periodically for any changes. Changes to this Privacy Policy are effective when they are posted 
        on this page."""
    )

# ---- PROJECTS ----
# with st.container():
#     st.write("---")
#     st.header("My Projects")
#     st.write("##")
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_lottie_animation)
#     with text_column:
#         st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
#         st.write(
#             """
#             Learn how to use Lottie Files in Streamlit!
#             Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
#             In this tutorial, I'll show you exactly how to do it
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
# with st.container():
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_contact_form)
#     with text_column:
#         st.subheader("How To Add A Contact Form To Your Streamlit App")
#         st.write(
#             """
#             Want to add a contact form to your Streamlit website?
#             In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/KEIFCORP@GMAIL.COM" method="POST">
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
