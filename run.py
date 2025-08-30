from app import create_app
from app.db import init_db_data

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        init_db_data()
    app.run(host="0.0.0.0", port=5000, debug=True)
