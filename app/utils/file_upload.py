import os
import uuid

from flask import current_app
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp"
}


def save_image(file, folder):
    """
    Save an uploaded image and return the filename.

    Args:
        file: Uploaded FileStorage object
        folder: Folder inside static/uploads
                e.g. "news", "hero", "gallery"

    Returns:
        filename or None
    """

    if not file:
        return None

    if file.filename == "":
        return None

    filename = secure_filename(file.filename)

    if "." not in filename:
        return None

    extension = filename.rsplit(".", 1)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        return None

    filename = f"{uuid.uuid4().hex}.{extension}"

    upload_folder = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        folder
    )

    os.makedirs(upload_folder, exist_ok=True)

    file.save(
        os.path.join(upload_folder, filename)
    )

    return filename