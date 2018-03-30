from flask import Flask
import os
application = Flask(__name__)

@application.route("/")
def hello():
	# return all environment variables
	environment = "Hello World!\n"
	for key, value in os.environ.items():
		environment += str(key) + ":" str(value) + ";\n"
    return environment

if __name__ == "__main__":
    application.run()
