# 📸 Instagram Auto Poster

An automated Instagram Reel posting system built with Python that uploads videos from Google Drive, tracks them using Google Sheets, and publishes them to Instagram on a predefined schedule.

## 🚀 Features

- 📁 Fetch videos from Google Drive
- 📊 Track upload status using Google Sheets
- 🎥 Automatically upload Instagram Reels
- ⏳ Wait until Instagram finishes processing
- ✅ Mark uploaded videos as `Posted`
- 📅 Automatic scheduling using APScheduler
- 🕖 Weekdays: 7:00 PM IST
- 🌞 Weekends: 10:00 AM & 7:00 PM IST

## 🛠️ Tech Stack

- Python
- Google Drive API
- Google Sheets API
- Instagram Graph API
- APScheduler

## 📂 Project Structure

```
instagram-auto-poster/
│
├── app/
│   ├── services/
│   ├── scheduler.py
│   ├── main.py
│   └── config.py
│
├── logs/
├── temp/
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Setup

1. Clone the repository
2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Configure environment variables.
4. Add your Google service account credentials.
5. Run the scheduler.

```bash
python -m app.scheduler
```

## 📌 Workflow

```
Google Drive
      │
      ▼
Google Sheets (Pending)
      │
      ▼
Scheduler
      │
      ▼
Instagram Graph API
      │
      ▼
Publish Reel
      │
      ▼
Update Google Sheet (Posted)
```

## 🔮 Future Enhancements

- AI-generated captions
- AI-generated hashtags
- Automatic Drive sync
- Better logging and retry mechanism
- Dashboard for monitoring uploads

---

Made with ❤️ using Python.