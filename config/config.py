import environs
import aiogram
env = environs.Env()

env.read_env()
token = env.str('BOT_TOKEN')
admins = env.list('ADMINS')