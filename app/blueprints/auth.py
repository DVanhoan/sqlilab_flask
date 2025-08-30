from flask import Blueprint, render_template, request, flash
from ..db import get_db
from ..services.user_service import login_vulnerable, login_safe

bp = Blueprint("auth", __name__, url_prefix="")

@bp.route("/vuln/login", methods=["GET", "POST"])
def vuln_login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        user, executed = login_vulnerable(get_db(), username, password)
        if user:
            flash(f"✅ Vulnerable login SUCCESS. Hello {user['username']}")
        else:
            flash("❌ Invalid credentials (vulnerable).")
        return render_template("login.html", mode="vuln", executed_sql=executed, username=username)
    return render_template("login.html", mode="vuln")

@bp.route("/safe/login", methods=["GET", "POST"])
def safe_login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        user, executed, bindings = login_safe(get_db(), username, password)
        if user:
            flash(f"✅ Safe login SUCCESS. Hello {user['username']}")
        else:
            flash("❌ Invalid credentials (safe).")
        return render_template("login.html", mode="safe", executed_sql=executed, bindings=bindings, username=username)
    return render_template("login.html", mode="safe")
