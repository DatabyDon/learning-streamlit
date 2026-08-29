# Notes - Learning Streamlit

# 0. Purpose
I'm a data nerd and love a good visualization. I tend to see a large amount of tools that solve for the 'final deliverable'. Wether that's a dashboard, report, or app, we have so many tools to choose from. As someone who has used Snowflake, I've heard a lot about Streamlit and had to try it out. What most excited me was the concept of using Streamlit as a BI-as-Code solution. This would elevate version control and remove limits on customization. Let's see if it's "lit" (sorry had to).

# 1. Playing Around
First off I went through Streamlit's [Playground](https://streamlit.io/playground). From a simple welcome page to an LLM chat, there were 6 different pre-built examples. These gave me an idea of what was really possible with this tool. 

I also noticed the syntax had simple, self-explanatory functions that easily described what I wanted to display. Want a button? `st.button` Want to make a line chart from data in a table? `[table_name].line_chart`. My first thoughts are that this will be an easy language to memorize syntax and easy to read if I have to come back to something or hand over the code.