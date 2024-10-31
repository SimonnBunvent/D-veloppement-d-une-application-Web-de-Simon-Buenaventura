from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

create_bp = Blueprint('create', __name__)

@create_bp.route('/createproject')
def createproject():
    return render_template('create/createproject.html')