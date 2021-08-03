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
            models.insert_delete_db(insert)

    if request.method == 'DELETE':
        pass

    if request.method == 'PUT':
        pass

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


@app.route('/', methods=['DELETE'])
def delete_student():
    id = request.form.get('id')
    print(id)
    if id:
        delete = f'''DELETE FROM alunos
        WHERE id = {id}'''
        print(delete)
        models.insert_delete_db(delete)


@app.route('/', methods=['PUT'])
def update_student():
    pass


if __name__ == '__main__':
    app.run(debug=True)
    delete_student()
