from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

create_bp = Blueprint('artists', __name__)


def artists():
    return render_template('artists/ppl.html')