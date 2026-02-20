# 📘 AI Health Coach – Project Documentation

## 1. Project Overview

AI Health Coach is a Flask-based web application integrated with Google Gemini API. It collects user health inputs and generates AI-powered personalized health analysis and recommendations.

---

## 2. Tech Stack

* Backend: Python (Flask)
* AI Model: Google Gemini API
* Frontend: HTML5, CSS3 (Glassmorphism + Animated UI)
* Environment Management: python-dotenv

---

## 3. Folder Structure

```
AI_Health_Coach/
│
├── app.py
├── agent.py
├── config.py
├── .env
│
├── templates/
│   ├── index.html
│   ├── form.html
│   ├── result.html
│   └── chat.html
│
├── static/
│   └── style.css
│
├── project_docs/
│   └── PROJECT_DOCUMENTATION.md
│
└── README.md
```

---

## 4. Application Flow

1. User lands on Home Page (index.html)
2. Navigates to Health Form
3. Submits personal health details
4. Backend processes request
5. Gemini API generates AI response
6. Results displayed in styled report page
7. Optional: Chat mode allows conversational health assistance

---

## 5. Environment Setup

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
```

---

## 6. Running the Application

Install dependencies:

```
pip install flask google-generativeai python-dotenv
```

Run app:

```
python app.py
```

Visit:

```
http://127.0.0.1:5000/
```

---

## 7. Features

* AI-generated personalized health summary
* Modern glassmorphism UI
* Animated gradient background
* Chat-based AI interaction
* Responsive design

---

## 8. Future Enhancements

* Voice integration
* AI streaming responses
* User login system
* Database storage
* Health analytics dashboard
* PDF report generation

---

## 9. Security Considerations

* API keys stored in .env
* Never expose keys in frontend
* Use HTTPS in production

---

## 10. Author

Developed as an AI-powered health assistant project.
