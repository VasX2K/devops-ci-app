"""HTTP-приложение для CI."""
from flask import Flask, jsonify

def create_app():
    """Создаёт приложение."""
    application = Flask(__name__)

    @application.get("/health")
    def health():
        """Проверяет жизнеспособность."""
        return jsonify(status="ok")

    @application.get("/")
    def index():
        """Возвращает сведения о службе."""
        return jsonify(service="devops-ci-app", version="1.0.1", status="running")

    return application

app = create_app()
