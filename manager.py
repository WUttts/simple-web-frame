from src import app_run
from flask_script import Manager, Server
import os

config_name = os.environ.get('FLASK_CONFIG') or 'Dev'
app = app_run(config_name)

manager = Manager(app)
manager.add_command("runserver", Server(use_debugger=True))

if __name__ == '__main__':
    manager.run()
