import psycopg2


def connect_db():
    db = psycopg2.connect(dbname='faculdade',
                          user='postgres',
                          password='',
                          host='localhost',
                          port='5433')

    return db


def create_table(sql):
    con = connect_db()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()


def query_db(sql):
    con = connect_db()
    cur = con.cursor()
    cur.execute(sql)

    recset = cur.fetchall()

    regis = []

    for rec in recset:
        regis.append(rec)

    con.close()

    return regis


def insert_delete_db(sql):
    con = connect_db()
    cur = con.cursor()

    try:
        cur.execute(sql)
        con.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        con.rollback()
        con.close()
        return 1

    cur.close()


if __name__ == '__main__':
    # sql = 'DROP TABLE  IF EXISTS public.alunos;'

    # create_table(sql)

    # sql = '''CREATE TABLE IF NOT EXISTS public.alunos(
    #     id INTEGER PRIMARY KEY NOT NULL,
    #     name VARCHAR(30),
    #     turm VARCHAR(10)
    # );
    # '''

    # create_table(sql)

    sql = 'SELECT * from alunos;'

    persons = query_db(sql)

    print(persons)
