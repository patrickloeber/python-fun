import sqlite3
from typing import List
import datetime
from model import Todo

conn = sqlite3.connect('todos.db')
c = conn.cursor()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS todos (
            task text,
            category text,
            date_added text,
            date_completed text,
            status integer,
            position integer
            )""")


create_table()


def insert_todo(todo: Todo):
    c.execute('select count(*) FROM todos')
    count = c.fetchone()[0]
    todo.position = count if count else 0
    with conn:
        c.execute('INSERT INTO todos VALUES (:task, :category, :date_added, :date_completed, :status, :position)',
        {'task': todo.task, 'category': todo.category, 'date_added': todo.date_added,
         'date_completed': todo.date_completed, 'status': todo.status, 'position': todo.position })


def get_all_todos() -> List[Todo]:
    c.execute('select * from todos')
    results = c.fetchall()
    todos = []
    for result in results:
        todos.append(Todo(*result))
    return todos


def delete_todo(position):
    c.execute('select count(*) from todos')
    count = c.fetchone()[0]

    with conn:
        c.execute("DELETE from todos WHERE position=:position", {"position": position})
        for pos in range(position+1, count):
            change_position(pos, pos-1, False)


def change_position(old_position: int, new_position: int, commit=True):
    c.execute('UPDATE todos SET position = :position_new WHERE position = :position_old',
                {'position_old': old_position, 'position_new': new_position})
    if commit:
        conn.commit()


def update_todo(position: int, task: str, category: str):
    with conn:
        if task is not None and category is not None:
            c.execute('UPDATE todos SET task = :task, category = :category WHERE position = :position',
                      {'position': position, 'task': task, 'category': category})
        elif task is not None:
            c.execute('UPDATE todos SET task = :task WHERE position = :position',
                      {'position': position, 'task': task})
        elif category is not None:
            c.execute('UPDATE todos SET category = :category WHERE position = :position',
                      {'position': position, 'category': category})


def complete_todo(position: int):
    with conn:
        c.execute('UPDATE todos SET status = 2, date_completed = :date_completed WHERE position = :position',
                  {'position': position, 'date_completed': datetime.datetime.now().isoformat()})
