from app.database.Models.UserPS import User
from app.utils import helpers

create = User(
    username='admin',
    email='admin@falafel.local',
    password=helpers.hash_create('admin')
)

