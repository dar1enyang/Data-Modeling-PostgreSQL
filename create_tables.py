import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    The funnction to create database
    
    Returns:
        cur  : Use the connection to get a cursor that will be used to execute queries.
        conn : The connection towards current connecting database.
    """
    
    # connect to database
    conn = psycopg2.connect("host=127.0.0.1 dbname=project_postgre user=dar1en password=")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS p1database")
    cur.execute("CREATE DATABASE p1database WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to the database
    conn = psycopg2.connect("host=127.0.0.1 dbname=p1database user=dar1en password=")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    The funnction to drop database
    
    Parameters:
        cur  : The cursor that will be used to execute queries.
        conn : The connection towards current connecting database.
    """
    
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    The funnction to drop database
    
    Parameters:
        cur  : The cursor that will be used to execute queries.
        conn : The connection towards current connecting database.
    """
    
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()