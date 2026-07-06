from flask import Blueprint, render_template
from flask_login import login_required

from app.models import News, Gallery, HeroSlide

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/")

def dashboard():

    stats = {
        "news": News.query.count(),
        "gallery": Gallery.query.count(),
        "slides": HeroSlide.query.count(),
    }

    return render_template(
        "admin/dashboard.html",
        stats=stats
    )