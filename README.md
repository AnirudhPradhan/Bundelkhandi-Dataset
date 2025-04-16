# 🗣️ Bundelkhandi-Dataset

This repository contains scripts and pipelines for Automatic Speech Recognition (ASR), Speaker Diarization, and video-to-audio conversion tailored to process and analyze audio data, specifically for the Bundelkhandi language dataset.

- 🖥️ **Fetching YouTube Videos** 📹🔗 – Download videos from YouTube for processing.
- 🎥 **Video to Audio Conversion** 🎬🔊 – Extracting high-quality audio from video files.
- 🎙️ **Speaker Diarization** 🗣️🔍 – Identifying and segmenting different speakers in an audio file.
- 📝 **Automatic Speech Recognition (ASR)** 🎤📝 – Transcribing speech into text with high accuracy.
- 🔗 **Pipeline Integration** 🔄⚙️ – Seamlessly combining these functionalities into an efficient workflow.

---

## 🚀 Getting Started

### 🛠️ Setup

#### 1️⃣ Clone the Repository 🖥️📂
```bash
git clone https://github.com/AnirudhPradhan/Bundelkhandi-Dataset.git
cd Bundelkhandi-Dataset
```

#### 2️⃣ Create a Virtual Environment (Recommended) 🏗️🐍
```bash
python -m venv venv
# Activate the virtual environment:
source venv/bin/activate  # On macOS and Linux
venv\Scripts\activate  # On Windows
```

#### 3️⃣ Install Dependencies 📦⚡
```bash
pip install -r requirements.txt
```
---

## 🎯 Usage

### 1️⃣ Run the Complete Pipeline 🚀🔄

- Open the **Jupyter Notebook** `main.ipynb` to execute each step of the full processing pipeline **manually**.

- For a **one-click transcript generation**, use `pipeline.ipynb` — simply update the YouTube video link and select the desired language:

### 2️⃣ Run Individual Components 🔧🛠️
Each functionality can also be executed separately:

- **Fetch YouTube Videos** 📹🔗
  ```bash
  python ScrapYTAudio.py
  ```
- **Convert Video to Audio** 🎥➡️🔊
  ```bash
  python VideoToAudio.py
  ```
- **Perform Speaker Diarization** 🗣️🔍
  ```bash
  python Diarization.py
  ```
- **Run Automatic Speech Recognition (ASR)** 🎤📝
  ```bash
  python ASR.py
  ```

Alternatively, check the **Jupyter Notebooks** 📓🔬 for detailed explanations and examples.

---

## 🤝 Contributing 💡🚀
We welcome contributions! If you'd like to improve the project, feel free to:

- Submit a **Pull Request** 📌🔧
- Open an **Issue** 🐛📢 for bug reports or feature suggestions
- Share feedback to enhance the repository 🚀💬

---

## 📜 License 📝🔓
For any questions or support, feel free to reach out! 🚀😊

