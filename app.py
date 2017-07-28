import cherrypy
import psycopg2


class Root():

    @cherrypy.expose
    def index(self):
        return 'index'


@cherrypy.expose
class Messages():

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

    def add_message(self, mess_id, message):
        dbname = cherrypy.config['database']['dbname']
        username = cherrypy.config['database']['user']
        conn = psycopg2.connect(dbname + ' ' + username)
        cursor = conn.cursor()

    def get_message(self, mess_id):
        dbname = cherrypy.config['database']['dbname']
        username = cherrypy.config['database']['user']
        conn = psycopg2.connect(dbname + ' ' + username)
        cursor = conn.cursor()


def run():
    cherrypy.config.update('server.cfg')
    cherrypy.tree.mount(Root(), '/')
    cherrypy.tree.mount(Messages(), '/messages', 'app.cfg')
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    run()
