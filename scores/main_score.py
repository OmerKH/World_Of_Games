from flask import Flask
from utils import BAD_RETURN_CODE, SCORES_FILE_NAME


# display in HTML

app = Flask(__name__)


@app.route("/")
def score_server():
    score = "0"
    try:
        with open(SCORES_FILE_NAME, "r", encoding="utf-8") as file:

            score = file.read().strip()
            if not score.isdigit():
                return f"""
                    <html>
                        <head>
                            <title>Score Game</title>
                        </head>
                        <body>
                            <h1>Error</h1>
                            <div id="score" style="color:red;">{BAD_RETURN_CODE}</div>
                        </body>
                    </html>
                """
            else:
                return f"""
                    <html>
                        <head>
                            <title>Score Game</title>
                        </head>
                        <body>
                            <h1>The score is:</h1>
                            <div id="score">{score}</div>
                        </body>
                    </html>
                """
    except FileNotFoundError:
        return f"""
        <html>
            <head>
                <title>Score Game</title>
            </head>
            <body>
                <h1>Error</h1>
                <div id="score" style="color:red;">{BAD_RETURN_CODE}</div>
            </body>
        </html>
        """
