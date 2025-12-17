# AI Resume to Portfolio Website Generator 🚀

An end-to-end **AI-powered web application** that automatically converts a user’s **resume into a fully functional portfolio website** using **Large Language Models (LLMs)**.

The application extracts resume content, understands user requirements, and generates **separate HTML, CSS, and JavaScript files**, packaged into a downloadable ZIP file.

---

## 🔥 Features

* 📄 Upload resume in **PDF or TXT format**
* 🧠 Resume-aware website generation using **LLMs**
* 🎨 Clean and professional **portfolio website layout**
* 📁 Generates **separate frontend files**:

  * `index.html`
  * `style.css`
  * `script.js`
* 📦 One-click **ZIP download**
* ⚡ Simple and intuitive **Streamlit UI**

---

## 🛠 Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Google Gemini LLM**
* **PyPDF2** (PDF text extraction)
* **HTML, CSS, JavaScript**

---

## 🧩 Project Architecture

```
Resume Upload (PDF/TXT)
        ↓
Text Extraction (PyPDF2)
        ↓
Prompt Engineering (LangChain)
        ↓
Gemini LLM
        ↓
HTML + CSS + JS Generation
        ↓
ZIP Download
```

---

## 🚀 How It Works

1. User uploads a resume (PDF/TXT)
2. User enters a requirement (e.g., “Create a modern portfolio website”)
3. The application:

   * Extracts resume content
   * Combines it with the user prompt
   * Sends structured instructions to the LLM
4. The LLM generates frontend code
5. The website files are zipped and ready for download

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ai-resume-to-portfolio-generator.git
cd ai-resume-to-portfolio-generator
```

### 2️⃣ Create virtual environment (optional)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set environment variables

Create a `.env` file:

```
gemini=YOUR_GOOGLE_GEMINI_API_KEY
```

### 5️⃣ Run the app

```bash
streamlit run app.py
```

---

## 📌 Example Prompt

```
Create a modern personal portfolio website highlighting my skills,
projects, experience, and contact details based on my resume.
```

---

## 🎯 Learning Outcomes

* Built a **document-aware GenAI application**
* Learned **LLM prompt structuring**
* Integrated **LangChain with Gemini**
* Developed **end-to-end Streamlit applications**
* Implemented **AI-based code generation**

---

## 🔮 Future Enhancements

* DOCX resume support
* Multiple website themes
* React / Tailwind code generation
* Direct deployment to Netlify / Vercel
* Resume section customization

---

## 👤 Author

**Aditya Swamy**
Aspiring Data Analyst | AI & Automation Enthusiast

---

⭐ If you like this project, feel free to star the repository!
