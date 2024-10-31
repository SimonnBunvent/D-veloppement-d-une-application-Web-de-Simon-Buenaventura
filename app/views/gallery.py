from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

create_bp = Blueprint('gallery', __name__)


def gallery():
    return render_template('artworks.html')