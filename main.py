import streamlit as st
import os
import zipfile
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from PyPDF2 import PdfReader

# Load environment variables
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

st.set_page_config(page_title="AI Resume to Website Generator", page_icon="😊")
st.title("AI Resume → Portfolio Website Generator")

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])

# User query
prompt = st.text_area("What do you want to build based on this resume?")

# Function to extract resume text
def extract_text(file):
    if file.type == "application/pdf":
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    else:
        return file.read().decode("utf-8")

if st.button("Generate Website"):
    if uploaded_file is None or prompt.strip() == "":
        st.warning("Please upload a resume and enter a prompt")
    else:
        resume_text = extract_text(uploaded_file)

        system_prompt = f"""
You are an expert frontend web developer and UI/UX designer.

Using the RESUME CONTENT and USER REQUIREMENT below,
generate a professional, responsive PORTFOLIO WEBSITE.

STRICT RULES:
- Generate ONLY frontend code
- Create THREE separate files:
  index.html
  style.css
  script.js
- Do NOT add explanations
- Do NOT use markdown
- Follow the exact output format

OUTPUT FORMAT:
--html--
[html code]
--html--

--css--
[css code]
--css--

--js--
[javascript code]
--js--

RESUME CONTENT:
{resume_text}

USER REQUIREMENT:
{prompt}
"""

        messages = [("system", system_prompt)]

        messages.append(("user",prompt))

        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
        response = model.invoke(messages)

        # Save files
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(response.content.split("--html--")[1])

        with open("style.css", "w", encoding="utf-8") as f:
            f.write(response.content.split("--css--")[1])

        with open("script.js", "w", encoding="utf-8") as f:
            f.write(response.content.split("--js--")[1])

        # Zip files
        with zipfile.ZipFile("portfolio_website.zip", "w") as zipf:
            zipf.write("index.html")
            zipf.write("style.css")
            zipf.write("script.js")

        st.download_button(
            "Download Portfolio Website",
            data=open("portfolio_website.zip", "rb"),
            file_name="portfolio_website.zip"
        )

        st.success("Website generated successfully!")
