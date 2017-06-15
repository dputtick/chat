import cherrypy


class Root():

    @cherrypy.expose
    def index(self):
        return "Hello world"


def config():
    conf = {
        'global': {
            'server.socket_host': 'localhost',
            'server.socket_port': 8000,
            # 'environment': production
        }
    }
    return conf


if __name__ == '__main__':
    conf = config()
    cherrypy.quickstart(Root(), '/', conf)
