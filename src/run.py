from flask.helpers import url_for

from core import app

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    print(url_for("api.company.list"))
