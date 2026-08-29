# Notes - Learning Streamlit

Follow along here: [Streamlit documentation](https://docs.streamlit.io/)

## Purpose
I'm a data nerd and love a good visualization. I tend to see a large amount of tools that solve for the 'final deliverable'. Wether that's a dashboard, report, or app, we have so many tools to choose from. As someone who has used Snowflake, I've heard a lot about Streamlit and had to try it out. What most excited me was the concept of using Streamlit as a BI-as-Code solution. This would elevate version control and remove limits on customization. Let's see if it's "lit" (sorry had to).

# [Installation](https://docs.streamlit.io/get-started/installation)

## Local Development

### [Playing Around](https://docs.streamlit.io/get-started/installation/streamlit-playground)
First off I went through Streamlit's [Playground](https://streamlit.io/playground). From a simple welcome page to an LLM chat, there were 6 different pre-built examples. These gave me an idea of what was really possible with this tool. 

I also noticed the syntax had simple, self-explanatory functions that easily described what I wanted to display. Want a button? `st.button` Want to make a line chart from data in a table? `[table_name].line_chart`. My first thoughts are that this will be an easy language to memorize syntax and easy to read if I have to come back to something or hand over the code.

### [Install](https://docs.streamlit.io/get-started/installation/command-line)
Set up was pretty easy if you've ever installed a library for python before, especially using a virtual environment. I used the command line for this. I used .venv for this project so I could:

1. Follow along with the documentation
2. Keep all subsequent packages in one place as I explore and build

I created my first [app](app.py) in this step as well. A simple "Hello World". To my surpise, when I ran the app my browser added a tab where I could see my newly created app with "Hello World" sitting there alone on the page. Quick context, I've never built sites or apps from code, all things have been analytics. So if this is normal, excuse my excitement. This is going to be fun!

## Cloud Development

I'm skipping this section for now since my main focus is building. My environments will change over time.  I will come back to this section and try both Github Codespaces for personal projects and Snowflake for enterprise proof of concepts. I'll mark the Installation section as "Done" for now.

# [Fundamentals](https://docs.streamlit.io/get-started/fundamentals)

## [Basic Concepts](https://docs.streamlit.io/get-started/fundamentals/main-concepts)

### **[Development Flow](https://docs.streamlit.io/get-started/fundamentals/main-concepts#development-flow)**

```mermaid
flowchart TD
    A[Write Code] --> B[Save]
    B --> C[Streamlit Detects Change]
    C --> D[Rerun App]
    D --> E[View Result]
    E --> A
```
This flow works really well having my editor on one side and my brower on the other as suggested by Streamlit's docs. This proved to be an easy workflow when I tested it with my app.py I previously made.

1. **Activated my virtual environment**
2. **Ran my app**
3. **Updated the app** from `Hello World!` → `Hello Worlds!`
4. **Saved the app file**
5. **Refreshed my browser**
6. **The app was updated. That simple.**
7. **Ctrl+C to stop Streamlit server**
8. **Deactivate venv**

### **[Data Flow](https://docs.streamlit.io/get-started/fundamentals/main-concepts#data-flow)**

```mermaid
flowchart TD
    A[Streamlit App Running] --> B{What triggers an update?}

    B -->|Change source code| C[Rerun entire script]
    B -->|User interacts with widget| D{Callback?}

    D -->|Yes| E[Run Callback First]
    E --> C

    D -->|No| C

    C --> F[Script runs top to bottom]
    F --> G[Updated UI]
```
Since python already uses sequential execution (running from top to bottom), this doesn't change how I write my scripts. That's great and let's me code the way I normally do.

### **[Display & Style Data](https://docs.streamlit.io/get-started/fundamentals/main-concepts#display-and-style-data)**

In this section I created a file for each demonstration and will share notes under each.

Write App
- uses `st.write()` to display some sample data provided in the documentation