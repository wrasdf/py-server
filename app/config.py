# import logging
import os


POSTGRES = {
    'user': 'postgres',
    'pw': 'password1',
    'db': 'pyserver',
    'host': 'postgres',
    'port': '5432',
}

# POSTGRES = {
#     'user': os.getenv('APPLICATION_POSTGRES_USER', 'postgres'),
#     'pw': os.getenv('APPLICATION_POSTGRES_PW', ''),
#     'host': os.getenv(
#         'APPLICATION_POSTGRES_HOST',
#         os.getenv('%s_PORT_5432_TCP_ADDR' % DB_CONTAINER)
#     ),
#     'port': os.getenv(
#         'APPLICATION_POSTGRES_PORT',
#         os.getenv('%s_PORT_5432_TCP_PORT' % DB_CONTAINER)
#     ),
#     'db': os.getenv('APPLICATION_POSTGRES_DB', 'postgres'),
# }

DB_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

# logging.basicConfig(
#     filename=os.getenv('SERVICE_LOG', 'server.log'),
#     level=logging.DEBUG,
#     format='%(levelname)s: %(asctime)s \
#         pid:%(process)s module:%(module)s %(message)s',
#     datefmt='%d/%m/%y %H:%M:%S',
# )
