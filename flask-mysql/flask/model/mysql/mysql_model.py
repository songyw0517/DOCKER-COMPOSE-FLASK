from mysql.connector import pooling
import mysql.connector
from flask import Flask, current_app, g
import os
class MysqlModel:
    def init_db(self, config=None):
        # initialize path
        query_path = '../mysql/sqls/initialize.sql'
        with open(query_path) as init_query:
            init_query = init_query.read().split(';')
        # database connect
        db = mysql.connector.pooling.MySQLConnectionPool(
            **current_app.config['DATABASE_CONFIG']
        )
        db_con = db.get_connection()
        db_cursor = db_con.cursor()

        # execute query
        for query in init_query:
            db_cursor.execute(query)
        db_cursor.fetchall()

        current_app.logger.info("Initialize Database")

    def register_connection(app:Flask):
        # 매 요청을 처리하기 전에 -> 데이터베이스 연결
        @app.before_request
        def register_connection():
            if 'db' not in g:
                g.db=mysql.connector.pooling.MySQLConnectionPool(
                    **current_app.config['DATABASE_CONFIG']
                )
            current_app.logger.info("Get MySQL connection pool...")
        
        # 매 요청을 처리한 후 -> 데이터베이스 연결 끊기
        @app.teardown_appcontext
        def close_connection(res):
            db = g.pop('db', None)
            if db is not None:
                db_con = db.get_connection()
                current_app.logger.info("Close MySQL connection pool")
                db_con.close()
            
    def get_connection(app):
        if 'db' not in g:
            connectionPool = mysql.connector.pooling.MySQLConnectionPool(**current_app.config['DATABASE_CONFIG'])
            g.db=connectionPool
        return g.db