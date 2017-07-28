import cherrypy
import psycopg2


class Root():

    @cherrypy.expose
    def index(self):
        return 'index'


@cherrypy.expose
class Messages():

    def __init__(self):
        self.dbname = cherrypy.config['dbname']
        self.username = cherrypy.config['user']

    def GET(self):
        if cherrypy.session.get('messages', None):
            messages = ' '.join(cherrypy.session['messages'])
        else:
            messages = 'No messages'
        return messages

    def POST(self, message=None):
        if not cherrypy.session.get('messages', None):
            cherrypy.session['messages'] = []
        cherrypy.session['messages'].append(message)
        message_len = str(len(message))
        return message_len

    def add_message(self, mess_id, message):
        conn = psycopg2.connect(self.dbname + ' ' + self.username)
        cursor = conn.cursor()

    def get_message(self, mess_id):
        conn = psycopg2.connect(self.dbname + ' ' + self.username)
        cursor = conn.cursor()


def run():
    cherrypy.config.update('server.cfg')
    cherrypy.tree.mount(Root(), '/')
    cherrypy.tree.mount(Messages(), '/messages', 'app.cfg')
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    run()
