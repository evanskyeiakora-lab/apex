from flask import render_template
from flask_login import login_required

from . import admin_bp
from app.models import News, Gallery, Member, ContactMessage


@admin_bp.route("/")
@login_required
def dashboard():

    return render_template(
        "admin/dashboard.html",
        news_count=News.query.count(),
        gallery_count=Gallery.query.count(),
        member_count=Member.query.count(),
        message_count=ContactMessage.query.count()
    )