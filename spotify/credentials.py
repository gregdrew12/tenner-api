import environ

env = environ.Env()
environ.Env.read_env('./.env')

CLIENT_ID = env('CLIENT_ID')
CLIENT_SECRET = env('CLIENT_SECRET')
REDIRECT_URI = env('REDIRECT_URI')
