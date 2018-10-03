from simpledu.app import create_app, db
from simpledu.models import User, Course, Chapter

app = create_app('development')


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Course': Course, 'Chapter': Chapter}


if __name__ == '__main__':
    app.run()
