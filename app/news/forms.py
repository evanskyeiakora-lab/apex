from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed

from wtforms import (
    StringField,
    TextAreaField,
    SelectField,
    SubmitField
)

from wtforms.validators import (
    DataRequired,
    Length
)


class NewsForm(FlaskForm):

    title = StringField(
        "News Title",
        validators=[
            DataRequired(),
            Length(max=255)
        ]
    )

    content = TextAreaField(
        "Content",
        validators=[
            DataRequired()
        ]
    )

    featured_image = FileField(
        "Featured Image",
        validators=[
            FileAllowed(
                ["jpg", "jpeg", "png", "webp"],
                "Only JPG, PNG and WEBP images are allowed."
            )
        ]
    )

    status = SelectField(
        "Publication Status",
        choices=[
            ("draft", "Draft"),
            ("published", "Published")
        ],
        default="draft"
    )

    submit = SubmitField("Save News")