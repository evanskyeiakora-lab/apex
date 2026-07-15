from datetime import datetime

from slugify import slugify

from app.extensions import db


class News(db.Model):
    __tablename__ = "news"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(255),
        nullable=False
    )

    slug = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    content = db.Column(
        db.Text,
        nullable=False
    )

    featured_image = db.Column(
        db.String(255),
        nullable=True
    )

    status = db.Column(
        db.String(20),
        default="draft",
        nullable=False
    )

    published_at = db.Column(
        db.DateTime,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def generate_slug(self):
        """
        Generate a unique slug from the title.
        """
        base_slug = slugify(self.title)
        slug = base_slug
        counter = 1

        while News.query.filter(
            News.slug == slug,
            News.id != self.id
        ).first():

            slug = f"{base_slug}-{counter}"
            counter += 1

        self.slug = slug

    def publish(self):
        self.status = "published"

        if not self.published_at:
            self.published_at = datetime.utcnow()

    def __repr__(self):
        return f"<News {self.title}>"