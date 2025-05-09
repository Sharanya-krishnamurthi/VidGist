# 🎬 VidGist — YouTube Video Summarizer

**VidGist** helps you quickly understand the core message of any YouTube video by extracting its transcript and generating a concise summary using state-of-the-art NLP models.

---

## 🚀 Features

- 🔗 Paste any YouTube video link
- 📝 Automatically fetches the transcript
- 🧠 Summarizes using a Transformer-based model (DistilBART)
- 💻 Clean and responsive Gradio web UI
- ⏱️ Saves time by letting you skip full videos

---

## 🛠️ Tech Stack

| Tool                   | Purpose                             |
|------------------------|-------------------------------------|
| Python                 | Core logic                          |
| Gradio                 | User Interface                      |
| Hugging Face Transformers | Text summarization model         |
| YouTube Transcript API | Extracting captions/transcripts     |
| PyTorch                | Backend framework for inference     |

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Sharanya-krishnamurthi/VidGist.git
cd VidGist
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

A browser window will automatically open with the VidGist UI.

---

## 📦 requirements.txt

```txt
transformers>=4.35.0
torch>=2.0.0
gradio>=4.0.0
youtube-transcript-api>=0.6.1
```

---

## 📸 Example

**Input:**

> [https://www.youtube.com/watch?v=example\_id](https://www.youtube.com/watch?v=example_id)

**Output:**

> Summary: This video discusses...

---

## 🧠 Model Used

* **Model**: `sshleifer/distilbart-cnn-12-6`
* **Framework**: Hugging Face Transformers
* **Task**: Abstractive summarization of natural language text

---


## ⚠️ Limitations

* Only works with videos that have publicly available transcripts
* May return errors for private, restricted, or non-captioned videos
* Summarization quality depends on transcript clarity

---

## 📜 License

MIT License © \Sharanya Krishnamurthi

---

