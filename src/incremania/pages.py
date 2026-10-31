from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)


@bp.get("/")
def home():
    return render_template(
        "pages/home.html",
        title="Flask + uv",
    )


@bp.get("/test")
def test():
    return render_template(
        "pages/test.html",
        title="Test new Site",
    )
