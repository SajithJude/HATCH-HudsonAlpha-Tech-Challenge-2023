import streamlit as st
from streamlit.components.v1 import components

st.set_page_config(
    page_title="My Glassmorphism Page",
    page_icon=":eyeglasses:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define styles
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #ec008c, #fc6767);
            color: white;
        }
        .glassmorphism {
            background: rgba(255, 255, 255, 0.3);
            border-radius: 20px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 300px;
            width: 100%;
            margin: 30px 0;
            padding: 50px;
        }
        .tab-content {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
        }
        .tab-column {
            width: 45%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Define components
menu = components.html(
    """
    <nav style="background: rgba(255, 255, 255, 0.3); padding: 20px;">
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Contact</a>
    </nav>
    """
)

sidebar = components.html(
    """
    <div style="background: rgba(255, 255, 255, 0.3); padding: 20px;">
        <h2>Sidebar</h2>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
        </ul>
    </div>
    """
)

main_content = components.html(
    """
    <div class="glassmorphism">
        <h1>Main Tab Content</h1>
        <div class="tab-content">
            <div class="tab-column">
                <div class="glassmorphism">
                    <h2>Card 1</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut pretium nibh non tellus euismod, eget euismod tellus aliquam. Duis efficitur dolor eros, id posuere urna congue vitae.</p>
                </div>
            </div>
            <div class="tab-column">
                <div class="glassmorphism">
                    <h2>Card 2</h2>
                    <p>Phasellus euismod arcu vel sapien vulputate auctor. Morbi tristique nunc in urna suscipit, eget suscipit neque semper. Aenean rhoncus tellus sed nulla iaculis, ut varius nunc gravida.</p>
                </div>
            </div>
        </div>
    </div>
    """
)

# Render components
components.html(menu)
components.html(sidebar)
components.html(main_content)
