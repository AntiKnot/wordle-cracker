from webui import WebUI  # Add WebUI to your imports
from flask import Flask, render_template, request

app = Flask(__name__)
ui = WebUI(app, debug=True)  # Create a WebUI instance

# all of your standard flask logic

if __name__ == '__main__':
    ui.run()  # replace app.run() with ui.run(), and that's it
