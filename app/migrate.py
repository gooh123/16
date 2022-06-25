import os
import json


from app import db, models

from sqlalchemy.sql import exists


def load(file_path):
    """
    ЗАГРУЖАЕТ КОНТЕНТ

    :param file_path:путь до файла
    :return:данные или пустой список
    """
    connect = []
    if os.path.isfile(file_path):
        with open(file_path) as file:
            connect = json.load(file)

    return connect


def migrate_user_roles(fixture_path):
    fixture_content = load(fixture_path)

    for role in fixture_content:

        if db.session.query(models.UserRole).filter(models.UserRole.id == role['id']).first is None:
            new_role = models.UserRole(**role)
            db.session.add(new_role)

    db.session.commit()


def users(fixture_path):
    fixture_content = load(fixture_path)

    for user in fixture_content:

        if db.session.query(models.User).filter(models.User.id == user['id']).first is None:
            new_role = models.User(**user)
            db.session.add(new_role)

    db.session.commit()
