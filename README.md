# LifeRPG: Human Stat Tracker 🚀

A Python/Django application designed to gamify personal growth. Track real-life activities, gain XP, and visualize your progress through a character stat sheet.

## 📊 Core Stats
- **Strength (STR):** Physical health and fitness.
- **Intelligence (INT):** Learning, reading, and cognitive skills.
- **Charisma (CHA):** Social interactions and networking.

## 🛠️ Tech Stack
- **Language:** Python 3.12+
- **Framework:** Django
- **Database:** SQLite (Development)
- **Visuals:** Chart.js (Planned for Radar Charts)

## 🚀 How to Run Locally

1. **Activate Virtual Environment:**
   ```bash
   # Windows
   .venv\Scripts\activate
   # Mac/Linux
   source .venv/bin/activate

2. **Install Dependencies:**
   ```bash
    pip install -r requirements.txt

3. **Run Migrations:**
   ```bash
    python manage.py migrate

4. **Start the Server:**
   ```bash
    python manage.py runserver

Access the app at http://127.0.0.1:8000/

📅 Roadmap
[x] Initial Django Setup

[ ] Create Profile Model with Stats

[ ] Build XP Calculation Logic

[ ] Implement Radar Chart Visualization

[ ] Add Social Feed / Leaderboard