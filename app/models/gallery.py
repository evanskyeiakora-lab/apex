from datetime import datetime

from app.extensions import db


class Gallery(db.Model):
    __tablename__ = "gallery"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(255),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    image = db.Column(
        db.String(255),
        nullable=False
    )

    category = db.Column(
        db.String(100),
        default="General"
    )

    is_featured = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Gallery {self.title}>"