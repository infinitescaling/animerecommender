import os
from flask import Flask
import random_anime as r_anime

#initialization
app = Flask(__name__)
app.config.update(
        DEBUG = True,
    )

# controllers
@app.route("/")

def random_anime():
    return "Go watch " + r_anime.pick_random()

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

