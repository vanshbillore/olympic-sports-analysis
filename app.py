from flask import Flask, render_template

app = Flask(__name__)

# ---- Tableau Public links (edit here if a dashboard name is different) ----
BASE = "https://public.tableau.com/views/GlobalOlympicSportPerformanceProject/"
STORY_URL = BASE + "GlobalOlympicSports"
DASH1_URL = BASE + "OlympicPerformanceDashboard"
DASH2_URL = BASE + "InvestmentandMedalInsights"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/insights")
def insights():
    return render_template("insights.html")


@app.route("/dashboard1")
def dashboard1():
    return render_template("embed.html", title="Dashboard 1: Olympic Performance",
                           subtitle="Medal trend, top countries, average medals per athlete and host nation medals.",
                           url=DASH1_URL)


@app.route("/dashboard2")
def dashboard2():
    return render_template("embed.html", title="Dashboard 2: Investment and Medal Insights",
                           subtitle="Investment vs medals, regional efficiency, sport categories, medal types and world map.",
                           url=DASH2_URL)


@app.route("/story")
def story():
    return render_template("embed.html", title="Olympic Story",
                           subtitle="A three-scene story answering the questions of Priya, Carlos and William.",
                           url=STORY_URL)


if __name__ == "__main__":
    app.run(debug=True)
