from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config  # ✅ Fixed import

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register blueprints
    from controllers.auth_controller import auth_bp
    from controllers.guest_controller import guest_bp
    from controllers.episode_controller import episode_bp
    from controllers.appearance_controller import appearance_bp

    # Assign URL prefixes
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(guest_bp, url_prefix="/guests")
    app.register_blueprint(episode_bp, url_prefix="/episodes")
    app.register_blueprint(appearance_bp, url_prefix="/appearances")

    # Root route
    @app.route("/")
    def index():
        return jsonify({"message": "🎬 Late Show API is running!"})

    return app

# App entry point
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
