from app import create_flask_app
from config import config
import click

application = create_flask_app(config)


# @application.cli.command('init-db')
# def init_db():
#     """First, run the Database init controller"""
#     mysql.MysqlModel.init_db(config)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=50505, debug=True)