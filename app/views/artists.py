from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

artists_bp = Blueprint('artists', __name__, url_prefix='/artists')

@artists_bp.route('/ppl')
def artist():
    # Se déconnecter consiste simplement à supprimer le cookie session
    return render_template('artists/ppl.html')