import os
import psycopg2


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
                host="localhost",
                database=os.environ['DB_NAME'],
                user=os.environ['DB_USERNAME'],
                password=os.environ['DB_PASSWORD'])

    def run_transaction(self, *args, **kwargs):
        # Open a cursor to perform database operations
        cur = self.conn.cursor()

        # Execute a command: this creates a new table
        cur.execute('DROP TABLE IF EXISTS books;')
        cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                        'title varchar (150) NOT NULL,'
                                        'author varchar (50) NOT NULL,'
                                        'pages_num integer NOT NULL,'
                                        'review text,'
                                        'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                        )

        # Insert data into the table

        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)',
                    ('A Tale of Two Cities',
                    'Charles Dickens',
                    489,
                    'A great classic!')
                    )


        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)',
                    ('Anna Karenina',
                    'Leo Tolstoy',
                    864,
                    'Another great classic!')
                    )

        self.conn.commit()

        cur.close()
        self.conn.close()