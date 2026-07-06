from datetime import datetime
from flask_login import UserMixin

from .extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class News(db.Model):
    __tablename__ = "news"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    slug = db.Column(db.String(220), unique=True)

    summary = db.Column(db.Text)

    content = db.Column(db.Text)

    image = db.Column(db.String(255))

    published = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Gallery(db.Model):
    __tablename__ = "gallery"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150))

    image = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class HeroSlide(db.Model):
    __tablename__ = "hero_slides"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200))

    subtitle = db.Column(db.Text)

    image = db.Column(db.String(255))

    button_text = db.Column(db.String(50))

    button_link = db.Column(db.String(255))

    active = db.Column(db.Boolean, default=True)