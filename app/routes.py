from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favorites')
def favorites():
    days_of_the_work_week = [
        {
            'day': 'Monday',
            'color': 'primary'
        },
        {
            'day': 'Tuesday',
            'color': 'secondary'
        },
        {
            'day': 'Wednesday',
            'color': 'success'
        },
        {
            'day': 'Thursday',
            'color': 'danger'
        },
        {
            'day': 'Friday',
            'color': 'warning'
        },   
    ]
    return render_template('fav_five.html', favorites=days_of_the_work_week)
