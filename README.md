# Learning Streamlit

Working through the official [Get Started Streamlit documentation](https://docs.streamlit.io/) end to end and I'll be sharing as I go. This repo is my public log of the process, part of the [DataByDon](#) learning series.

## Why Streamlit?

As I continue building toward AI Integration / Applied AI Engineering, Streamlit is the fastest way to turn data and ML work into something people can actually click through. Steamlit is:


🌐 **Free & Open-source** – Community-driven development.

🐍 **Python-native** – Built entirely in Python.

⚡ **Fast** – Optimized for high performance.

🌀 **Dynamic** – Adapts to your data in real-time.

This is a hands-on pass through the docs rather than a single project — the goal is fluency with the core API and concepts before I lean on it inside bigger builds.

## Progress 📈

Using the **Get started** section — checklist mirrors its structure on docs.streamlit.io down to the sub-page level. I'll check items off as I work through them and link to the relevant script/notebook in this repo where applicable. More sections (Develop, Deploy, Knowledge base) will get added here as the series continues.

### 🏷️ Status Legend

| Emoji | Meaning | Description |
| :---: | :--- | :--- |
| ✅ | **Done** | Completed and documented this section. |
| ✍️ | **In Progress** | Section I'm currently working on. |
| ➖ | **Skipped/Removed** | Writing or updating documentation. |
| [ ] | **Not Started** | Writing or updating documentation. |

### 🚀 Get started
- [x] Installation
  - ✅ Local development
    - ✅ Use Streamlit Playground
    - ✅ Install via command line
    - ➖ Install via Anaconda Distribution
  - ➖ Cloud development
    - ➖ Use GitHub Codespaces
    - ➖ Use Snowflake
- [ ] Fundamentals
  - ✅ Basic concepts
  - ✍️ Advanced concepts
  - [ ] Additional features
  - [ ] Summary
- [ ] First steps
  - [ ] Create an app
  - [ ] Create a multipage app

## Repo Structure

> Still settling on the final layout — updating this as the pattern solidifies.

```
learning-streamlit/
├── README.md
└── notes.md
└── first_app.py
└── basic/
  └── magic.py          # Uses magic commands to display a dataframe
  └── write.py          # Uses st.write to create dataframe
  └── dfstyler.py       # Dataframe formatting with Styler
  └── line_chart.py     # Simple line chart based on data
  └── map.py            # Simple map based on lat & lon data
  └── layout.py         # Created a left panel and columns of widgets
  └── progress.py       # Created a loading progress bar
└── advanced/

```

## Resources

- [Streamlit docs](https://docs.streamlit.io/)
- [Streamlit API cheat sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)
- [Streamlit app gallery](https://streamlit.io/gallery)
- [Streamlit community forum](https://discuss.streamlit.io/)

---

Check out my other projects at [DataByDon](#)