import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    test database connectivity, drops database with name sparkifydb,
    and starts a new connection to sparkifydb with the following parameters:
        host: localhost
        dbname: sparkifydb
        user: postgres
        password: posDS123
    :return: None
    """
    # connect to default database
    conn = psycopg2.connect("host=localhost dbname=studentdb user=postgres password=posDS123")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # This code is to terminate all connections to this db except my own
    # Reference: https://stackoverflow.com/questions/17449420/postgresql-unable-to-drop-database-because-of-some-auto-connections-to-db
    cur.execute("REVOKE CONNECT ON DATABASE sparkifydb FROM public;")
    cur.execute("""
    SELECT pid, pg_terminate_backend(pid) 
    FROM pg_stat_activity 
    WHERE datname = current_database() AND pid <> pg_backend_pid();
    """)

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=localhost dbname=sparkifydb user=postgres password=posDS123")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    drops tables by looping through all the tables to drop them
    :param cur: postgreSQL cursor
    :param conn: function that refers to db connection
    :return: None
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    create postgreSQL tables
    :param cur: postgreSQL cursor
    :param conn: function that refers to db connection
    :return: None
    """
    # looping through each item being sql create command
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    START of the program. Holds database connection and cursor.
    First drops tables then creates them for reuse.
    :return: None
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()