from flask import Flask, render_template, request
import models

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        new_id = request.form.get('id')
        new_person = request.form.get('name')
        new_turm = request.form.get('turm')

        if new_id and new_person and new_turm:
            insert = f'''INSERT INTO alunos(id, name, turm)
            VALUES ({new_id},'{new_person}', '{new_turm}');'''
            models.insert_delete_update_db(insert)

    persons = '''SELECT * FROM alunos;'''
    persons_ = models.query_db(persons)

    try:

        person_data = []

        for person in persons_:

            p = {
                'id': person[0],
                'name': person[1],
                'turm': person[2]
            }

            person_data.append(p)

        return render_template('formulario.html', person_data=person_data)

    except Exception:
        message = 'Have one person with this ID'
        return {'status': 'Error', 'message': message}


@app.route('/delete_student', methods=['GET', 'POST'])
def delete_student():
    if request.method == 'POST':
        id = request.form.get('id')
        print(id)
        if id:
            delete = f'''DELETE FROM alunos
            WHERE id = {id};'''
            print(delete)
            models.insert_delete_update_db(delete)

    persons = '''SELECT * FROM alunos;'''
    persons_ = models.query_db(persons)

    try:

        person_data = []

        for person in persons_:

            p = {
                'id': person[0],
                'name': person[1],
                'turm': person[2]
            }

            person_data.append(p)

        return render_template('delete_student.html', person_data=person_data)

    except Exception:
        message = 'Have one person with this ID'
        return {'status': 'Error', 'message': message}


@app.route('/update_student', methods=['GET', 'POST'])
def update_student():
    if request.method == 'POST':
        id = request.form.get('id')
        new_person = request.form.get('name')
        new_turm = request.form.get('turm')

        if id and new_person and new_turm:
            queries = f'SELECT id FROM alunos WHERE id = {id};'
            queries = models.query_db(queries)

            if queries == []:
                message = 'Unknown Id'
                return {'status': 'Error', 'message': message}

            update = f'''UPDATE alunos
            SET name = '{new_person}', turm = '{new_turm}'
            WHERE id = {id};'''

            models.insert_delete_update_db(update)

    persons = '''SELECT * FROM alunos;'''
    persons_ = models.query_db(persons)

    try:

        person_data = []

        for person in persons_:

            p = {
                'id': person[0],
                'name': person[1],
                'turm': person[2]
            }

            person_data.append(p)

        return render_template('update_student.html', person_data=person_data)

    except Exception:
        message = 'Have one person with this ID'
        return {'status': 'Error', 'message': message}


if __name__ == '__main__':
    app.run(debug=True)
