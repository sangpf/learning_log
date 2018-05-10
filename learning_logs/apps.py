from django.apps import AppConfig


class LearningLogsConfig(AppConfig):
    name = 'learning_logs'

import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())
application = app.wsgifunc()

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()


