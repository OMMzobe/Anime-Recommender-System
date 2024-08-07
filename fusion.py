# fusion.py

import streamlit as st
from streamlit_option_menu import option_menu
from search1 import search_page_content
import random

# The main function where we will build the actual app
def main():
    # Set up the page configuration
    st.set_page_config(page_title="Fusion-X Network", page_icon=":smile:", layout="wide", initial_sidebar_state="expanded")

    # Define custom CSS
    css = """
    <style>
    /* Style the sidebar */
    .css-1d391kg {
        background-color: #f0f0f0;
    }
    .css-1d391kg .css-1v3fvcr {
        color: #333;
    }
    /* Style the selected menu item */
    .css-1d391kg .css-1v3fvcr a {
        color: #02ab21;
        font-weight: bold;
    }
    /* Hover effect for menu items */
    .css-1d391kg .css-1v3fvcr a:hover {
        background-color: #e0e0e0;
    }
    .video-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 70vh;
        width: 100%;
        overflow: hidden;        
    }
    .video-container iframe {
        width: 100%;
        height: 80vh;
        border: none;
    }
    .anime-row {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        padding: 20px;
        gap: 20px;
    }
    .anime-item {
        flex: 0 0 auto;
        text-align: center;
    }
    .anime-item img {
        width: 200px;
        height: 300px;
        object-fit: cover;
        border-radius: 10px;
    }
    .anime-item button {
        margin-top: 10px;
        background-color: #02ab21;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
    }
    .anime-item button:hover {
        background-color: #029e1a;
    }
    .star-rating {
        color: #FFD700;
        font-size: 20px;
        display: inline-block;
        padding: 2px;
    }
    .feedback-page {
        background-image: url('dragenballs.jpg');  /* Replace with your image URL */
        background-size: cover;
        padding: 20px;
    }
    .feedback-comment {
        background-color: rgba(173, 216, 230, 0.8);
        color: black;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .eda-explanation {
        background-color: rgba(173, 216, 230, 0.8);
        color: black;
        padding: 10px;
        border-radius: 5px;
        margin-top: 20px;
    }
    </style>
    """

    # Inject the CSS
    st.markdown(css, unsafe_allow_html=True)
    
    # Page selection
    if 'logged_in' not in st.session_state:
        st.session_state.page = 'login'
    elif 'current_profile' not in st.session_state:
        st.session_state.page = 'profile'
    else:
        st.session_state.page = 'home'

    def verify_credentials(username, password):
        return True  # You should implement your own verification logic here

    def login_content():
        st.image("company_logo.jpeg")
        st.title("Welcome to FusionX-Network")
        st.title("SIGN IN")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        st.write("Don't have an account? Sign up")
        st.write("Forgot password?")
        if st.button("Login"):
            st.write()
            # Verify login credentials
            if verify_credentials(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.page = 'profile'

    def profile_content():
        st.title(f"Welcome, {st.session_state.username}!")
        st.title("Who's watching?")

        # List of names
        names = ["Kevin", "Lucy", "Add Profile"]
        # Show three profiles with anime images
        profiles = [
            "https://mrwallpaper.com/images/high/anime-profile-luffy-looking-up-39w1ckv07redydbx.webp", 
            "https://mrwallpaper.com/images/high/anime-profile-uzumaki-naruto-evhdy1dkbrz8c9ni.webp", 
            "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/New_user_icon-01.svg/512px-New_user_icon-01.svg.png?20160211171440"
        ]
        for i, (profile, name) in enumerate(zip(profiles, names)):
            with st.container():
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.title(name)
                    st.write(f"Click to view {name}'s profile")
                    if st.button("View Profile", key=f"profile_button_{name}"):
                        if name == "Add Profile":
                            st.write("This feature is coming soon!")
                        else:
                            st.session_state.current_profile = name.lower().replace(' ', '_')
                            st.session_state.page = 'home'
                with col2:
                    st.image(profile, width=300)
                    st.write("---")
    
    def home_content():        
        selection = option_menu(
            menu_title=None,
            options=["Home", "Search", "EDA", "Feedback"],
            icons=["house", "search", "bar-chart", "envelope"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            key="main_menu_home"
        )

        # Page routing based on the bar selection
        if selection == "Home":
            st.title("Anime Collection")

            # Video content
            video_html = """
            <div class="video-container">
                <iframe src="https://www.youtube.com/embed/eeZ1Ufdra0E?autoplay=1&mute=0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div>
            """
            st.markdown(video_html, unsafe_allow_html=True)
            
            # Anime content
            anime_sections = {
                "Your next watch": [
                    {"title": "Freeza: The beginning", "image": "freeza.png", "video": "path_to_video1.mp4"},
                    {"title": "Pokemon", "image": "pokemon.jpg", "video": "path_to_video2.mp4"},
                    {"title": "Freeza's Return", "image": "freeza2.png", "video": "path_to_video2.mp4"},
                    {"title": "War God", "image": "anime1.jpg", "video": "path_to_video1.mp4"},
                    # Add more anime details here...
                ],
                "Movies": [
                    {"title": "Dragen Ball Z: Evolution", "image": "dbz.png", "video": "path_to_video3.mp4"},
                    {"title": "Tekken", "image": "tekken.jpg", "video": "path_to_video4.mp4"},
                    {"title": "Kakarot", "image": "goku.jpeg", "video": "path_to_video4.mp4"},
                    {"title": "Yugioh", "image": "yugi.png", "video": "path_to_video4.mp4"},
                    # Add more anime details here...
                ],
                "Series": [
                    {"title": "One Punch Man", "image": "one punch man.jpg", "video": "path_to_video5.mp4"},
                    {"title": "Naruto:Evil Empire", "image": "harusho.png", "video": "path_to_video6.mp4"},
                    {"title": "King Vegita", "image": "vegita.png", "video": "path_to_video4.mp4"},
                    {"title": "Baki", "image": "baki.jpg", "video": "path_to_video5.mp4"},
                    # Add more anime details here...
                ],
            }

            for section, animes in anime_sections.items():
                st.header(section)
                cols = st.columns(len(animes))
                for col, anime in zip(cols, animes):
                    with col:
                        st.image(anime['image'], use_column_width=True)
                        st.markdown(f"**{anime['title']}**")
                        # Display static rating
                        rating = random.randint(1, 5)
                        st.markdown(f"""
                        <div class="star-rating">
                            {"&#9733;" * rating}{"&#9734;" * (5 - rating)}
                        </div>
                        """, unsafe_allow_html=True)
                        if st.button(f"Watch {anime['title']}", key=f"watch_{anime['title']}"):
                            # Replace the button with the link
                            st.markdown(f"[Watch Now]({anime['video']})", unsafe_allow_html=True)
        elif selection == "Search":
            search_page_content()  # Add your search page content or functionality here
        elif selection == "EDA":
            eda_content()  # Ensure `show()` is the correct function in `eda.py`
        elif selection == "Feedback":
            feedback_content()

    def feedback_content():
        st.title("Feedback Page")

        # Existing comments
        if 'comments' not in st.session_state:
            st.session_state.comments = [
                {"user": "Alice", "comment": "I really enjoyed Dragon Ball Z. The story and characters.", "rating": 5},
                {"user": "Bob", "comment": "It was okay, but the pacing was slow.", "rating": 3},
                {"user": "Charlie", "comment": "One man punch is not my cup of tea, but well made.", "rating": 2},
                {"user": "Diana", "comment": "Amazing visuals and soundtrack!'Vegita' is a must watch", "rating": 4}
            ]

        # Form for new feedback
        st.markdown("## Leave Your Feedback")
        user_feedback = st.text_area("Your Feedback", key="user_feedback")
        user_rating = st.slider("Your Rating", 1, 5, 3, key="user_rating")
        if st.button("Submit Feedback", key="submit_feedback"):
            new_comment = {
                "user": st.session_state.username,
                "comment": user_feedback,
                "rating": user_rating
            }
            st.session_state.comments.insert(0, new_comment)  # Add new comment to the beginning of the list
            st.experimental_rerun()  # Rerun to clear the feedback form

        # Display comments
        st.markdown("<div class='feedback-page'>", unsafe_allow_html=True)
        for comment in st.session_state.comments:
            st.markdown(f"""
            <div class="feedback-comment">
                <strong>{comment['user']}</strong>: {comment['comment']}
                <div class="star-rating">
                    {"&#9733;" * comment['rating']}{"&#9734;" * (5 - comment['rating'])}
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    def eda_content():
        st.title("Exploratory Data Analysis")
        
        # Top 10 Most Popular Anime Titles
        st.markdown("<h3 style='text-align: center;'>Top 10 Most Popular Anime Titles</h3>", unsafe_allow_html=True)
        st.image("Anime title viz.jpg", caption="Placeholder for picture", width=700)
        st.markdown("### Analysis:")
        st.markdown("""
        <div class='eda-explanation'>
            The chart highlights a diverse range of popular anime, with 'Death Note' leading in popularity, followed by 'Sword Art Online' and 'Shingeki no Kyojin.' Both classic and newer titles maintain strong appeal, indicating a dynamic anime landscape with engaged fanbases.
        </div>
        """, unsafe_allow_html=True)
        
        # Average Rating Per Genre Word Count
        st.markdown("<h3 style='text-align: center;'>Average Rating Per Genre Word Count</h3>", unsafe_allow_html=True)
        st.image("genre analysis.jpg", caption="Placeholder for picture", width=700)
        st.markdown("### Analysis:")
        st.markdown("""
        <div class='eda-explanation'>
            This visual quickly conveys which genres are most highly rated and popular. Notably, genres like Josei, Thriller, Police, and Psychological stand out for their high ratings, reflecting strong viewer engagement. The presence of a wide range of genres highlights diverse preferences, underscoring the need for personalized recommendations.
        </div>
        """, unsafe_allow_html=True)

        # Correlation Map
        st.markdown("<h3 style='text-align: center;'>Pie Chart</h3>", unsafe_allow_html=True)
        st.image("pie chart new.jpg", caption="Placeholder for picture", width=700)
        st.markdown("### Analysis:")
        st.markdown("""
        <div class='eda-explanation'>
            The pie chart visually represents the average number of episodes across different anime types, with TV series  dominating, indicating a preference for long-form content. ONAs  and movies  cater to users preferring shorter, binge-watchable content, suggesting a recommender system should offer a mix of TV series, ONAs, OVAs, specials, music-themed content, and movies to maximize user engagement.
        </div>
        """, unsafe_allow_html=True)

    # Page routing
    if st.session_state.page == 'login':
        login_content()
    elif st.session_state.page == 'profile':
        profile_content()
    elif st.session_state.page == 'home':
        home_content()
    elif st.session_state.page == 'feedback':
        feedback_content()

# Required to let Streamlit instantiate our web app.  
if __name__=='__main__':
    main()

