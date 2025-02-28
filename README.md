# 🍽 Foodies Day
## Restaurant Finder & Travel Guide

## 📌 About the Project
This is a **Django-based web application** that helps users find the top one day travel guide based on the best restaurants in a selected city using the **Google Places API Autocomplete** and **GEMINI API**. The app generates a **one-day travel guide** for the selected city using an AI-powered response system (Gemini API).

## 🚀 Features
- **Google Places API Autocomplete** for city selection
- **AI-generated travel guide** for a one-day itinerary
- **Dynamic loading screen** while AI processes the response

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2️⃣ Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the project's root directory and add your API keys:
```ini
GOOGLE_PLACES_API_KEY=your_google_api_key
GOOGLE_GEMINI_API_KEY=your_gemini_api_key
```

### 5️⃣ Run Database Migrations
```bash
python manage.py migrate
```

### 6️⃣ Start the Django Server
```bash
python manage.py runserver
```
The application will be available at **http://127.0.0.1:8000/**

---

## 🌍 APIs Used
### 🔹 Google Places API Autocomplete
- Used for **city selection**
- Ensures valid locations are chosen before search
- [Google Places API Docs](https://developers.google.com/places/web-service/intro)

### 🔹 Gemini API (Google AI)
- Generates a **custom travel guide** for the selected city
- Processes the city input and provides detailed responses
- [Gemini API Docs](https://ai.google.dev/)

---

## 🏗 Future Improvements
- 🌍 **Multi-language support**
- 📍 **More detailed travel itineraries**
- 📌 **Accept only inputs from AUTOCOMPLETE API**
- 🗺 **Interactive maps for restaurant locations**

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing
Pull requests are welcome! Feel free to fork the repository and submit PRs to improve the project. 🚀

