import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "./src/db/database.db"

    sql_create_shopping_list_table = """ CREATE TABLE IF NOT EXISTS shopping_list (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            created_date text,
                                            modified_date text
                                    ); """

    sql_create_article_table = """ CREATE TABLE IF NOT EXISTS articles (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        category text NOT NULL
                                );"""

    sql_create_list_article_table = """ CREATE TABLE IF NOT EXISTS list_article (
                                            shopping_list_id integer NOT NULL,
                                            article_id integer NOT NULL,
                                            quantity integer NOT NULL,
                                            FOREIGN KEY (shopping_list_id) REFERENCES shopping_list (id)
                                            FOREIGN KEY (article_id) REFERENCES articles (id)
                                    );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create shopping list table
        create_table(conn, sql_create_shopping_list_table)

        # create articles table
        create_table(conn, sql_create_article_table)

        # create list_article table
        create_table(conn, sql_create_list_article_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == "__main__":
    main()
