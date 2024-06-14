from urls import rules
from flasgger import Swagger
from core.utils import reserve
from flask import Flask
from users import users_app

app = Flask("Maktab_105", template_folder="templates")
app.register_blueprint(users_app, url_prefix="/users")

swagger = Swagger(app)

# serving url patterns
reserve(app, rules)


if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)
