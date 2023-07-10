from flask import Flask


def create_app():
  app = Flask(__name__)
  # encrypt cookie or session data
  app.config['SECRET_KEY'] = 'secure_NOTES_app'
  return app
