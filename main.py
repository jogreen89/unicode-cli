import click
import argparse
from pdb import set_trace
#from flask import Flask
#app = Flask(__name__)

#def create_app(config_filename):
#    app = Flask(__name__)
#    app.config.from_pyfile(config_filename)

#    from unicode_cli.model import db
#    db.init_app(app)
#    return

def greeting():
	""" greeting - process the command line arguments """
	parser = argparse.ArgumentParser(description="Process whale data")
	parser.add_argument("--data", help="csv data to ingest")

	args = parser.parse_args()
	set_trace()
	print(args)
	return

def process_data():
	""" process_data - processes the incoming csv data """
	return "Process Data func"

"""
@click.command()
@click.option("--count", default=1, help="Number of greetings")
@click.option("--name", prompt="Your name",
              help="The person to greet.")
def hello(count, name):
    for x in range(count):
        click.echo("Hello %s!" % name)
"""

# @app.route("/")

def run():
    return "Hello, World"

if __name__ == "__main__":
    # hello()
	greeting()

