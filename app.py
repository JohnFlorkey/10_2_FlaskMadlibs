from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'notmuchofasecret'

debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    return render_template('form.html', prompts=story.prompts)

@app.route('/story')
def show_story():
    story_text = story.generate(request.args)
    return render_template('story.html',story_text=story_text)