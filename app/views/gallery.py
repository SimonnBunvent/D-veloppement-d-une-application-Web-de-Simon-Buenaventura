from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

gallery_bp = Blueprint('gallery', __name__)

@gallery_bp.route('/artworks')
def artworks():
    return render_template('artworks.html')