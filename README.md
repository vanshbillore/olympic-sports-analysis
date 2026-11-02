# Global Olympic Sports Performance Analysis (Tableau + Flask)

Flask web application that embeds the published Tableau dashboards and story.

## Structure
    app.py            Flask routes and Tableau links
    templates/        HTML pages (base, home, about, insights, embed)
    static/css/       Stylesheet

## Run
    pip install -r requirements.txt
    python app.py
Open http://127.0.0.1:5000

## Pages
Home, About, Insights, Dashboard 1, Dashboard 2, Story.

## Data
Simulated dataset with the same structure as the project dataset: 60 countries, 50 sports, 1992 to 2026.
