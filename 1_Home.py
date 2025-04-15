import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Insightzen - Market Research Simplified", layout="wide", page_icon="/home/im/Insightzen_s.png")


st.sidebar.markdown(
    """
    <style>
    [data-testid="stSidebarCollapsedControl"] img {
        height: 70px;
        width: auto;
    }
    </style>
    <style>
    [data-testid="stSidebar"] img {
        height: 100px;
        width: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.logo(
"/home/im/Insightzen.png",
    link="http://insightzen.ir/",
    icon_image="/home/im/Insightzen_s.png",
)

# Main title section centered
st.markdown(
    """
    <h1 style='text-align: center; margin-bottom: 5px;'>Welcome to Insightzen</h1>
    <h2 style='text-align: center; font-size: 28px; font-weight: normal; color: #ff4955;'>Your All-in-One Market Research Companion</h2>
    """,
    unsafe_allow_html=True
)

# Introduction
st.markdown(
    """
    ## Empowering Market Research Professionals
    Insightzen is a cutting-edge web application designed specifically for researchers in the field of **market research**. 
    Whether you're working on a small independent project or managing a large-scale research initiative, **Insightzen** provides 
    all the tools you need to **collect, analyze, and generate valuable insights** efficiently. More than just an analytical tool, 
    Insightzen functions as a **comprehensive project management platform** tailored to the needs of market researchers.
    """
)

# Center the button using columns (hacky but works)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.link_button(
        label="Try it now",
        url="http://insightzen.ir/Product",
        type="primary",  # White text on primary color
        use_container_width=True  # Full-width button
    )

# Add an image before "Why Choose Insightzen?"
st.image("/home/im/Insightzen.gif", use_container_width=True)

# Why Choose Insightzen?
st.header("Why Choose Insightzen?")
st.markdown(
    """
    We believe that market research should be **accessible, efficient, and driven by data**. Insightzen streamlines every aspect 
    of the research process, helping you move from raw data to actionable insights seamlessly. Our platform is built to **accommodate 
    researchers of all backgrounds**, whether you're a seasoned data scientist or a professional with no programming experience.
    """
)

# Features Section
st.header("Everything You Need, All in One Place")

features = [
    ("📘 Learn Market Research", "/home/im/learn_market_research.jpg", "Gain access to essential resources, methodologies, and best practices to enhance your research skills."),
    ("🚀 Implement What You Learn", "/home/im/implement_what_you_learn.jpg", "Leverage built-in tools to execute your research strategies efficiently."),
    ("🛠️ Seamless Project Management", "/home/im/seamless_project_management.png", "Organize, track, and manage your research projects with ease, from data collection to final reporting."),
    ("🤖 Advanced AI-Powered Analytics", "/home/im/ai_powered_analytics.jpeg", "Utilize cutting-edge **artificial intelligence** models to process data faster and generate high-quality insights."),
    ("💡 User-Friendly for All", "/home/im/user_friendly.jpg", "If you're a **programmer**, you can integrate your own scripts and workflows to customize your research approach. If you're **not a programmer**, Insightzen is designed to be intuitive and easy to use without any coding knowledge.")
]

for i, (title, img, desc) in enumerate(features):
    col1, col2 = st.columns([1, 2]) if i % 2 == 0 else st.columns([2, 1])
    
    if i % 2 == 0:
        with col1:
            st.image(img, use_container_width=True)
        with col2:
            st.subheader(title)
            st.markdown(desc)
    else:
        with col1:
            st.subheader(title)
            st.markdown(desc)
        with col2:
            st.image(img, use_container_width=True)

# Market Research Importance
st.header("The Need for Market Research Has Never Been Greater")
st.markdown(
    """
    Today, **businesses of all sizes**, from startups to multinational corporations, as well as **government organizations**, rely on 
    market research to make data-driven decisions. Every move in today's competitive world is guided by a **target market**, and to successfully 
    enter that market, thorough research is essential. **Insightzen simplifies this process** so you can focus on **discovering trends, 
    understanding consumers, and making informed strategic decisions**.
    """
)

# Closing Statement
st.header("Let’s Learn Together, Let’s Do Together")
st.markdown(
    """
    Insightzen is more than just a tool—it’s a **community-driven platform** that empowers researchers to collaborate, innovate, and succeed. 
    Whether you’re exploring new markets, analyzing consumer behavior, or developing data-backed strategies, **Insightzen is your trusted partner** 
    in market research.
    
    ✨ **You just ask, we deliver. Your research, powered by AI.** ✨
    
    **Start your journey with Insightzen today and transform the way you approach market research!**
    """
)
