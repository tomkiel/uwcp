from os import listdir
from importlib import import_module
from fnmatch import fnmatch
from sqlalchemy import create_engine, orm, exc
from dynaconf import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
Session = orm.sessionmaker(bind=engine)
session = Session()
seeds = []
for file in listdir(settings.SEEDS_DIR):
    if(fnmatch(file, "*.py")) and (file != "__init__.py"):
        seeds.append('app.database.Seeds.' + file.replace('.py', ''))


def seed():
    """
    Seed initial database data
    """
    for seeder in seeds:
        module = import_module(seeder)
        element = getattr(module, 'create')
        try:
            session.add(element)
            session.commit()
            print('Success when running the Seeder ' + seeder)

        except exc.IntegrityError as error:
            session.rollback()
            print('Could not execute Seeder ' + seed + '. Data already exists?')

    print('All seeders running seccesfull!')


