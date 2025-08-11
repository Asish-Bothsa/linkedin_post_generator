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

```
## Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/Asish-Bothsa/linkedin_post_generator
   cd linkedin_post_generator
   ```
2. **Install dependencies:**
   - Make sure you have Python 3.10+ and [uv](https://github.com/astral-sh/uv) installed.
   - Install dependencies:
     ```sh
     uv pip install -r requirements.txt
     # or if using pyproject.toml
     uv pip install
     ```
3. **Set up API keys:**
   - Create a `.env` file in the project root with your LLM API keys:
     ```env
     OPENAI_API_KEY=your_openai_key_here
     # or
     GOOGLE_API_KEY=your_gemini_key_here
     ```
4. **Configure agents and tasks:**
   - Edit `config/agents.yaml` and `config/tasks.yaml` to customize agent behavior and tasks.
## Troubleshooting
- Ensure your API keys are valid and have access to the selected LLM provider.
- If you see authentication errors, double-check your `.env` file and restart your terminal.
- For C++ build errors on Windows, install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

## License
MIT


