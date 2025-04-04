from environs import Env

env = Env()
env.read_env()

# keys
secret_key = env.str("SECRET_KEY")
database_url = env.str("DATABASE_URL")
db_name = env.str("DATABASE_NAME")
db_user = env.str("DATABASE_USER")
db_password = env.str("DATABASE_PASSWORD")
db_host = env.str("DATABASE_HOST")
db_port = env.int("DATABASE_PORT")
