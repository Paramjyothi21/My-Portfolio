import streamlit as st
import json
import requests
import webbrowser
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title='ParamJyothi | Portfolio',page_icon=":desktop_computer:",layout="wide")

def load_lottiefile(filepath: str) :
     with open(filepath,"r") as f :
          return json.load(f)
     
def load_lottieurl(url) :
    r = requests.get(url)
    if r.status_code!=200 : return None
    return r.json()

lottie_animation1 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_2glqweqs.json")
lottie_animation2 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_78DCvgGZC7.json")
lottie_animation3 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_ddz8yrig.json")
lottie_animation4 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_7wJrqr.json")
lottie_animation5 = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_4m4xa6he.json")
lottie_animation6 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_lzhv1mc4.json")
lottie_animation7 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_aGFno30IGO.json")

selected = option_menu(
        menu_title = None,
        options = ["Home","Projects","Achievement"],
        icons = ["house","book","trophy"],
        menu_icon ="cast",
        default_index=0,
        orientation="horizontal",
    )
if selected == "Home" :

# Insert animation

     with st.container() :
          left1,middle1,right1 = st.columns(3)
          with middle1 : 
               st_lottie(lottie_animation1,height=300,key="programmer")
     st.markdown(
               '''<span lang="en">
               <h2 style="color:white"><i>I am Param Jyothi, an ASPIRING WEB DEVELOPER</i></h2>
               </span>''',
               unsafe_allow_html=True
               )
     st.write("---")

# Programming languages

     with st.container() :
          first,second = st.columns(2)
          with second : st_lottie(lottie_animation2,height=300,key="coding")
          with first :
               #st.markdown('<span style="color:red">This is red text</span>', unsafe_allow_html=True)
               st.markdown('<span style="color:white"><h2><i>Programming Languages</i></h2></span>',unsafe_allow_html=True)
               st.write(
                    """I can able to code in various programming languages.
                    Open to learn new languages and able to switch between programming languages quickly."""
               )
               """
               - Python
               - Java
               - C
               """
     st.write("---")

# Technologies

     with st.container() :
          left,right = st.columns(2)
          with right :
               st.markdown('<span style="color:white"><h2><i>Technologies</i></h2></span>',unsafe_allow_html=True)
               st.write(
                    """I'm familiar with Markup languages and scripts. 
               I am flexible and adaptive in learning new technologies."""
               )
               """
               - HTML
               - CSS
               - Javascript
               """
          with left : st_lottie(lottie_animation3,height=300,key="markup")  
     st.write("---")

# New Web 

if selected=="Projects" :
     with st.container() :
          col1,col2,col3 = st.columns([2,3,1])
          with col2 : 
               st.markdown('<span><h1 style="color:lightgrey">My PROJECTS</h1></span>',unsafe_allow_html=True)
     st.write("---")
# 1st Project

     st.markdown('<span style="color:white"><h2><i>1. Encryption Decryption Image Text</i></h2></span>',unsafe_allow_html=True)
     col1,col2 = st.columns([4,2])
     with col1 :
          st.write(
                    """
                    - Hide messages and images inside images.
                    - Includes both encryption and decryption of images.
                    - Can see the encrypted message by decrypting the image.
                    """
               )
          link_url = "https://github.com/Paramjyothi21/Encryption-Decryption-Image-Text"
          button_html = '''
                         <a href="{}" target="_blank">
                         <button style="padding: 5px 15px; background-color: #071114; color: white; border: outset; cursor: pointer;">
                         View project 1</button></a>
                         '''
          st.markdown(button_html.format(link_url), unsafe_allow_html=True)
          st.write("\n")
     with col2 :
          st_lottie(lottie_animation4,height=300,key="emotion")
     st.write("---")

# 2nd Project

     st.markdown('<span style="color:white"><h2><i>2. Visualization-Merge-Sort</i></h2></span>',unsafe_allow_html=True)
     col1,col2 = st.columns([4,2])
     with col1 :
          st.write(
                    """
                    - The Merge Sort algorithm first iteratively divides the array into equal partitions until each partition reduces to a single element. Then it combines them in the same manner as they were divided in an ordered way.
                    - It uses Divide and Conquer technique.
                    - the elements are sorted using the basic technique of comparison and swap. Finally, it merges all the elements together to get the final sorted list of data items.
                    """
               )
          link_url = "https://github.com/Paramjyothi21/Visualization-Merge-Sort"
          button_html = '''
                         <a href="{}" target="_blank">
                         <button style="padding: 5px 15px; background-color: #071114; color: white; border: outset; cursor: pointer;">
                         View project 2</button></a>
                         '''
          st.markdown(button_html.format(link_url), unsafe_allow_html=True)
          st.write("\n")
     with col2 :
          st_lottie(lottie_animation5,height=300,key="sort")
     st.write("---")

# 3rd Project 

     st.markdown('<span style="color:white"><h2><i>3. Cipher Text Conversion</i></h2></span>',unsafe_allow_html=True)
     col1,col2 = st.columns([4,2])
     with col1 :
          st.write(
                    """
                    - In this all characters of plain text is replaced by other characters with same pattern.
                    - A Caesar cipher is a simple method of encoding messages. Caesar ciphers use a substitution method where letters in the alphabet are shifted by some fixed number of spaces to yield an encoding alphabet. 
                    - A Caesar cipher with a shift of 1 would encode an A as a B, an M as an N, and a Z as an A, and so on.
                    """
               )
          link_url = "https://github.com/Paramjyothi21/Cipher-Text-Conversion"
          button_html = '''
                         <a href="{}" target="_blank">
                         <button style="padding: 5px 15px; background-color: #071114; color: white; border: outset; cursor: pointer;">
                         View project 3</button></a>
                         '''
          st.markdown(button_html.format(link_url), unsafe_allow_html=True)
          st.write("\n")
     with col2 :
          st_lottie(lottie_animation6,height=300,key="cipher")
     st.write("---")
          
# 4th Project 

     st.markdown('<span style="color:white"><h2><i>4. Rock paper scissor cut</i></h2></span>',unsafe_allow_html=True)
     col1,col2 = st.columns([4,2])
     with col1 :
          st.write(
                    """
                    - A Simple rock paper scissor cut game using python.
                    - Python tkinter, using gui's (Graphical user interface).
                    - Rock paper scissor cut with system.
                    """
               )
          link_url = "https://github.com/Paramjyothi21/Rock-Paper_Scissor-Cut"
          button_html = '''
                         <a href="{}" target="_blank">
                         <button style="padding: 5px 15px; background-color: #071114; color: white; border: outset; cursor: pointer;">
                         View project 4</button></a>
                         '''
          st.markdown(button_html.format(link_url), unsafe_allow_html=True)
          st.write("\n")
     with col2 :
          st_lottie(lottie_animation7,height=300,key="cut")
     col1,col2,col3,col4,col5 = st.columns(5)
     with col3 : 
          link_url = "https://github.com/Paramjyothi21"
          button_html = '''
                         <a href="{}" target="_blank">
                         <button style="padding: 5px 15px; background-color: #071114; color: white; border: outset; cursor: pointer;">
                         View all projects</button></a>
                         '''
          st.markdown(button_html.format(link_url), unsafe_allow_html=True)
     st.write("---")

# Acheivements

if selected=="Achievement" :
     with st.container() :
          col1,col2,col3 = st.columns([2,3,1])
          with col2 : 
               st.markdown('<span><h1 style="color:lightgrey">My ACHIEVEMENTS</h1></span>',unsafe_allow_html=True)
     st.write("---")
# 1. Leetcode
     col1,col2 = st.columns([5,1]) 
     with col1 :
          st.markdown('<span style="color:white"><h3><i>1. Leetcode profile</i></h3></span>',unsafe_allow_html=True)
          st.write(
               """
               - Paramjyothi21 - LeetCode Profile
               - Languages : Python, Java.
               - Participating in contests.
               """
          )
          link_url = "https://leetcode.com/paramjyothi567/"
          button_html = '''
                         <a href="{}" target="_blank">
                         <button style="padding: 5px 15px; background-color: #071114; color: white; border: outset; cursor: pointer;">
                         View Leetcode profile</button></a>
                         '''
          st.markdown(button_html.format(link_url), unsafe_allow_html=True)
          st.write("\n")
     with col2 :
          st.image("Images/leetcode.png",width=200)
     st.write("---")
# 2. GeeksforGeeks
     col1,col2 = st.columns([5,1]) 
     with col1 :
          st.markdown('<span style="color:white"><h3><i>2. Codechef</i></h3></span>',unsafe_allow_html=True)
          st.write(
               """
               - Paramjyothi21 | GeeksforGeeks 
               - Problem Solved : 100+.
               - Badges : Problem solver, Daily Streak
               - Data Structures & Algorithms, Basic Programming.
               - Languages : Python, C++, Java, C.
               """
          )
          link_url = "https://www.codechef.com/users/paramjyothi567"
          button_html = '''
                         <a href="{}" target="_blank">
                         <button style="padding: 5px 15px; background-color: #071114; color: white; border: outset; cursor: pointer;">
                         View Codechef profile</button></a>
                         '''
          st.markdown(button_html.format(link_url), unsafe_allow_html=True)
          st.write("\n")
     with col2 :
          st.image("Images/GFG.png",width=200)
     st.write("---")
# 3. HackerRank
     col1,col2 = st.columns([5,1]) 
     with col1 :
          st.markdown('<span style="color:white"><h3><i>3. HackerRank profile</i></h3></span>',unsafe_allow_html=True)
          st.write(
               """
               - Paramjyothi21 - HackerRank
               - Badges : Problem Solving, Java
               - Languages : Python, Java, C, MySQL, Problem Solving. (2)
               - Functional, Object oriented programming and Data structures and algorithms.
               """
          )
          link_url = "https://www.hackerrank.com/paramjyothi567"
          button_html = '''
                         <a href="{}" target="_blank">
                         <button style="padding: 5px 15px; background-color: #071114; color: white; border: outset; cursor: pointer;">
                         View Hackerrank profile</button></a>
                         '''
          st.markdown(button_html.format(link_url), unsafe_allow_html=True)
          st.write("\n")
     with col2 :
          st.image("Images/Hackerrank.png",width=200)
     col1,col2,col3 = st.columns([2,1,2])
     with col2 :
          link_url = "https://flowcv.com/resume/u97m12cndp"
          button_html = '''
                         <a href="{}" target="_blank">
                         <button style="padding: 5px 15px; background-color: #071114; color: white; border: outset; cursor: pointer;">
                         View My Resume</button></a>
                         '''
          st.markdown(button_html.format(link_url), unsafe_allow_html=True)
          st.write("\n\n\n")
     st.write("---")

# Contact Information
 
col1, col2, col3 = st.columns([2, 3, 1])
col1.write("")
col3.write("")
with col2 :
     st.markdown('<span style="color:white"><h2><i>Want to Contact me ?</i></h2></span>',unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 2])
with col2 :
     link_url = "https://www.linkedin.com/in/gummadivelli-paramjyothi-179b7122a/"
     button_html = '''
                    <a href="{}" target="_blank">
                    <button style="padding: 5px 15px; background-color: #071114; color: white; border: outset; cursor: pointer;">
                    LinkedIn</button></a>
                    '''
     st.markdown(button_html.format(link_url), unsafe_allow_html=True)
     st.write("\n")
with col3 :
     link_url = "https://github.com/Paramjyothi21"
     button_html = '''
                    <a href="{}" target="_blank">
                    <button style="padding: 5px 15px; background-color: #071114; color: white; border: outset; cursor: pointer;">
                    GitHub</button></a>
                    '''
     st.markdown(button_html.format(link_url), unsafe_allow_html=True)
     st.write("\n")
with col4 :
     link_url = "https://twitter.com/ChinniJyothi21"
     button_html = '''
                    <a href="{}" target="_blank">
                    <button style="padding: 5px 15px; background-color: #071114; color: white; border: outset; cursor: pointer;">
                    Twitter</button></a>
                    '''
     st.markdown(button_html.format(link_url), unsafe_allow_html=True)
     st.write("\n")
