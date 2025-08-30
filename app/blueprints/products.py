from flask import Blueprint, render_template, request, flash
from ..db import get_db
from ..services.product_service import (
    search_vulnerable, search_safe,
    list_vulnerable, list_safe
)

bp = Blueprint("products", __name__, url_prefix="")

@bp.route("/vuln/search")
def vuln_search():
    q = request.args.get("q", "")
    rows, executed = search_vulnerable(get_db(), q)
    if q:
        flash("🔎 Vulnerable search executed.")
    return render_template("search.html", mode="vuln", products=rows, q=q, executed_sql=executed)

@bp.route("/safe/search")
def safe_search():
    q = request.args.get("q", "")
    rows, executed, bindings = search_safe(get_db(), q)
    if q:
        flash("🔎 Safe search executed.")
    return render_template("search.html", mode="safe", products=rows, q=q, executed_sql=executed, bindings=bindings)

@bp.route("/vuln/products")
def vuln_products():
    order = request.args.get("order", "id")
    rows, executed, error = list_vulnerable(get_db(), order)
    if error:
        flash(f"❌ SQL Error: {error}")
    return render_template("products.html", mode="vuln", products=rows, order=order, executed_sql=executed, error=error)

@bp.route("/safe/products")
def safe_products():
    order = request.args.get("order", "id")
    rows, executed = list_safe(get_db(), order)
    return render_template("products.html", mode="safe", products=rows, order=order, executed_sql=executed)
