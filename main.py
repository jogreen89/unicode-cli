from flask import Flask
app = Flask(__name__)

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from unicode_cli.model import db
    db.init_app(app)

@app.route("/")
def run():
    return "Hello, World"

if __name__ == "__main__":
    run()

