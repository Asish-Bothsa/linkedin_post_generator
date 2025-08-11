# 🚀 LinkedIn Post Generator with CrewAI

An AI-powered multi-agent system that **generates optimized LinkedIn posts** by analyzing trends, creating content, enhancing engagement, and reviewing for quality — all automated using **CrewAI** and **Google Gemini**.

---

## 📌 Features

- **Multi-Agent Workflow** using CrewAI:
  - **Trend Analyst** → Identifies trending topics in the chosen domain.
  - **Content Creator** → Crafts engaging and well-structured LinkedIn posts.
  - **Engagement Optimizer** → Suggests improvements for higher reach (hashtags, tone, hooks).
  - **Post Reviewer** → Ensures grammar, clarity, and professional tone.

- **Sequential AI Pipeline** — Tasks run in order for maximum quality.
- **Customizable Agents & Tasks** via YAML configuration.
- **LLM Integration** with Google Gemini 2.0 Flash.


## 📂 Project Structure

```plaintext
linkedin_post_generator/
│
├── main.py                # Main CrewAI workflow
├── config/
│   ├── agents.yaml         # Agent configurations
│   └── tasks.yaml          # Task configurations
├── .env                    # Environment variables
└── requirements.txt        # Python dependencies


