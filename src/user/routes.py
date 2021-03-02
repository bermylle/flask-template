from flask import Blueprint, render_template

# Set up a Blueprint
sample_blueprint = Blueprint('sample_blueprint', __name__)

@sample_blueprint.route('/')
def index():
	return render_template('main.html')

@sample_blueprint.route('/About')
def about():
	
	return render_template('about.html')