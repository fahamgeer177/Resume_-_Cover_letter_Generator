# Resume_&_Cover_letter_Generator 🚀

An AI-powered Streamlit app that helps you quickly generate:
- Professional resumes 📄
- Personalized cover letters ✉️

Built for job seekers who want to tailor applications to a specific role with less effort and better quality.

## ✨ Features

- Resume Generator tailored to job description
- Cover Letter Generator tailored to job description
- Optional custom instructions for polishing output
- Simple, user-friendly Streamlit interface

## 🛠️ Tech Stack

- Python
- Streamlit
- OpenAI API

## 📂 Project Structure

- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/fahamgeer177/Resume_-_Cover_letter_Generator.git
cd Resume_&_Cover_letter_Generator
```

### 2. Create and activate a virtual environment

#### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your OpenAI API key 🔐

#### Windows (PowerShell)

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

#### macOS/Linux

```bash
export OPENAI_API_KEY="your_api_key_here"
```

## ▶️ Run the app

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`).

## 🧠 How to Use

1. Choose Resume Generator or Cover Letter Generator from the sidebar.
2. Enter position name and job description.
3. Optionally add extra instructions.
4. Click generate and copy your result.

## ⚠️ Important Notes

- Never commit real API keys to GitHub.
- If a key was previously exposed, rotate/revoke it immediately.
- This app currently uses the OpenAI SDK interface compatible with `openai==0.28.1`.

## 📌 Future Improvements

- Export to PDF/Docx 📥
- Save generation history 🗂️
- Add multiple tone/style templates 🎨
- Add ATS score hints 📊

## 🤝 Contributing

Contributions are welcome! Open an issue or submit a pull request.

## 📜 License

Add your preferred license here (for example, MIT).
