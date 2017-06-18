# The form uses the POST method.
# a regular input with type="text" and a textarea.
# Set name="rot" on the input element and name="text" on the textarea.
# Has a label on the input element that looks something like the one in the screenshot above.
# The input element has the default value of 0.

from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form method="POST">
                <label name="rotation-label">
                Rotate By
                <input type="text" name="rot" value="0" />
                <textarea type="text" name="text">{0}</textarea>
                </label>
                <input type="submit" value="Submit Query" />
            </form>
        </body>
    </html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    rot_input = int(request.form['rot'])
    text_area = request.form['text']
    return form.format(rotate_string(text_area, rot_input))

@app.route("/")
def index():
    return form.format("")

app.run()