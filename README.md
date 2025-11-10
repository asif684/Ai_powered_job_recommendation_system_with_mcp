# 🤖 AI Powered Job Recommendation System with MCP

🚀 **AI-Powered Career Assistant** that analyzes resumes, detects skill gaps, suggests career roadmaps, and recommends jobs from **Naukri** & **LinkedIn** — all powered by **EURI AI**, **Apify**, and **Streamlit**, with backend capabilities via **FastMCP**.

---

## 🧠 Key Features

✅ **Resume Intelligence**
- Extracts text from PDF resumes 🧾  
- Generates **AI summaries**, **skill gap analyses**, and **career roadmaps**

✅ **Smart Job Search**
- Fetches jobs dynamically from **Naukri** & **LinkedIn** using Apify Actors  
- Suggests best job titles & keywords using AI ⚙️  

✅ **MCP Integration**
- Exposes `fetch_naukri_jobs` via **FastMCP server**  
- Enables multi-client AI interaction

✅ **Modern UI**
- Beautiful, clean Streamlit web interface 💻  
- Animated spinners and responsive cards  

---

### 📁 Project Structure

```bash
AI_Powered_Job_Recommendation_System_with_MCP/
│
├── app.py                     # 🎨 Streamlit web app interface
├── mcp_server.py              # ⚙️ FastMCP server for job fetching
│
├── src/
│   ├── helper.py              # 📄 PDF text extraction + EURI AI interface
│   ├── job_api.py             # 🌐 Job data fetcher (Naukri & LinkedIn)
│
├── pyproject.toml             # 📦 Project metadata (uses uv)
├── requirements.txt           # 🧰 Dependencies
├── uv.lock                    # 🔒 UV lockfile for reproducible builds
└── README.md                  # 📘 Project documentation
```

---

## ⚙️ Tech Stack

| Category | Tools / Libraries |
|-----------|------------------|
| **Frontend** | 🧩 Streamlit |
| **Backend API** | ⚡ FastMCP |
| **AI Processing** | 🧠 EURI AI (`gpt-4.1-nano`) |
| **Job Data** | 🌐 Apify Actors (Naukri & LinkedIn) |
| **PDF Processing** | 📄 PyMuPDF (`fitz`) |
| **Env Management** | 🔐 dotenv |
| **Package Manager** | 🧵 [uv](https://github.com/astral-sh/uv) |

---

## 🧰 Installation (Using `uv`)

```bash
# 1️⃣ Clone the repository
git clone https://github.com/yourusername/AI_Powered_Job_Recommendation_System_with_MCP.git
cd AI_Powered_Job_Recommendation_System_with_MCP

# 2️⃣ Install dependencies using uv
uv sync

# 3️⃣ Activate environment
uv run python
```
---
### 🔑 Environment Setup

Create a `.env` file in the **project root** and add your API keys as shown below:

```bash
EURI_API_KEY=your_euri_api_key_here
APIFY_TOKEN=your_apify_token_here
```
---
### ▶️ Running the Project

#### 🖥️ Launch Streamlit App

```bash
uv run streamlit run app.py
```
---
Then open 👉 http://localhost:8501 in your browser.
---

## ⚡ Run MCP Server
---
```bash
uv run python mcp_server.py
```
---
### 🧩 Code Overview

#### 🧾 `src/helper.py`

Handles **PDF extraction** & **EURI AI calls**.

```python
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text
```
---
#### 🌐 `src/job_api.py`

Fetches jobs using **ApifyClient** for **LinkedIn** & **Naukri**.

```python
def fetch_naukri_jobs(search_query, location="india", rows=60):
    run_input = {"keyword": search_query, "maxJobs": 60}
    run = apify_client.actor("alpc").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs
```
---
#### 🎨 `app.py`

Streamlit front-end for **resume analysis** & **personalized job recommendations**.

```python
st.markdown('<h1 class="main-title">📄 AI Job Recommender </h1>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
```
---
### 🖥️ Displays

The application provides the following key insights:

- 📑 **Resume Summary**  
- 🛠 **Skill Gaps**  
- 🚀 **Career Roadmap**  
- 💼 **Job Recommendations**
---
#### ⚙️ `mcp_server.py`

Defines **MCP tool** for job data retrieval.

```python
@mcp.tool()
async def fetchnaukri(listofkey):
    return fetch_naukri_jobs(listofkey)
```
---
🧪 Example Workflow

- 📤 **Upload your resume (PDF)**
- 🤖 **AI summarizes your skills & experience**
- 🧩 **Detects missing skills or certifications**
- 🗺️ **Suggests a personalized roadmap**
- 💼 **Fetches job recommendations from Naukri**
---

### 📦 Dependencies
- streamlit
- openai
- pymupdf
- python-dotenv
- apify-client
- google-generativeai
---
### 🌍 Future Enhancements
- 🔮 Integration with LinkedIn live job APIs
- 🗂️ Skill-based clustering & visualization
- 💬 Chat-style career assistant
- 📊 Dashboard analytics for job trends

---
### 👨‍💻 Author

Mohammed Asif Ameen Baig
- 🎓 B.Tech in Robotics and Automation Engineering | GNA University
- 🌐 GitHub: asif684

---
### 🧡 Acknowledgments
- EURI AI — for LLM-powered API integration

- Apify — for job data scraping

- Streamlit — for rapid UI development

- uv — for blazing-fast dependency management
---
