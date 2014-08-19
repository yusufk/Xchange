from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Xchange'
settings.subtitle = 'local contact information exchange'
settings.author = 'Yusuf Kaka'
settings.author_email = 'yusufk@mailbox.co.za'
settings.keywords = 'contact exchange'
settings.description = ''
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'fd234ea3-65d2-4547-83dc-c9ca2f99df19'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'janrain'
settings.login_config = ''
settings.plugins = []
