#!/usr/bin/env python
from app import create_app, db
from app.models import Student

if __name__ == '__main__':
    app = create_app('development')
    with app.app_context():
        db.create_all()
    app.run()
