from app.extensions import db


class SiteSetting(db.Model):
    __tablename__ = "site_settings"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    site_name = db.Column(
        db.String(150),
        default="Apex Citizens of Ghana"
    )

    tagline = db.Column(
        db.String(255)
    )

    logo = db.Column(
        db.String(255)
    )

    favicon = db.Column(
        db.String(255)
    )

    email = db.Column(
        db.String(120)
    )

    phone = db.Column(
        db.String(30)
    )

    address = db.Column(
        db.Text
    )

    facebook = db.Column(
        db.String(255)
    )

    twitter = db.Column(
        db.String(255)
    )

    instagram = db.Column(
        db.String(255)
    )

    linkedin = db.Column(
        db.String(255)
    )

    youtube = db.Column(
        db.String(255)
    )

    footer_text = db.Column(
        db.Text
    )

    def __repr__(self):
        return f"<SiteSetting {self.site_name}>"