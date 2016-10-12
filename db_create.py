#!flask/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEYM_MIGRATE_REPO
from app import db
import os.path
db.create_all()
if not os.path.exists(SQLALCHEYM_MIGRATE_REPO):
	api.create(SQLALCHEYM_MIGRATE_REPO, 'database repository')
	api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEYM_MIGRATE_REPO)
else:
	avi.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEYM_MIGRATE_REPO, avi.version(SQLALCHEYM_MIGRATE_REPO))

