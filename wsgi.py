from app import app, socketio

if __name__ == "__main__":
    socketio.run(app)
    
# Gunicorn and wsgi(Web Server Gateway Interface) both are used for depolying python web application 
# ,particularly for apps built by django, Flask