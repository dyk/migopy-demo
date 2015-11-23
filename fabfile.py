import migopy

class Migrations(migopy.MigrationsManager):
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_USER = 'dyk'
    MONGO_USER_PASSWORD = 'mongo'
    MONGO_DATABASE = 'profile'

migrations = Migrations.create_task()
