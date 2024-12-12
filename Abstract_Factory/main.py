from flask import Flask, render_template, redirect, session, url_for
from decouple import config, Csv, UndefinedValueError
from maker_fact import MakerFactory
import json
app = Flask(__name__)
app.config['DEBUG'] = True  # Enable debug mode
app.secret_key = config('SECRET_KEY', cast=str)


    
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/config')
def config_page():
    os_type = config('OS', default='Unknown', cast=str)
    catalogue_str = config(f'{os_type}Catalogue', cast=str)

    try:
        maker_catalogue = json.loads(catalogue_str)
    except json.JSONDecodeError:
        return '<h1>Error: Invalid catalogue format in environment variable</h1>', 400
    
    try:
    # Use the factory to create the maker and store it in the session
        maker = MakerFactory.create_maker(os_type, maker_catalogue)
    except ValueError as e:
        return f'<h1>{e}</h1>', 405

    # Serialize only the essentials into the session
    session['os_type'] = os_type
    session['catalogue'] = maker_catalogue

    return redirect(url_for('maker_page'))
        
    
    

@app.route('/maker')
def maker_page():
    os_type = session.get('os_type')
    maker_catalogue = session.get('catalogue')

    if not os_type or not maker_catalogue:
        return redirect(url_for('config_page'))

    try:
        # Create the maker on demand using the factory
        maker = MakerFactory.create_maker(os_type, maker_catalogue)
    except ValueError as e:
        return f'<h1>{e}</h1>', 500

    items = maker.get_catalogue()
    print(f'items: {items}')
    return render_template('maker.html', items=items)

