from flask import Flask
import subprocess as sp

app = Flask(__name__)

@app.route("/")
def php():
    out = sp.run(["php", "php.php"] , stdout=sp.PIPE)
    return out.stdout
