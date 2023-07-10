from flask import Flask


def create_app():
  app = Flask(__name__)
  # encrypt cookie or session data
  app.config['SECRET_KEY'] = 'secure_NOTES_app'

  from .views import views
  from .auth import auth
  # register blueprint
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')

  return app
