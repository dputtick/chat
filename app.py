import cherrypy


class Root():

    @cherrypy.expose
    def index(self, message=None):
        if message:
            return message


def config():
    conf = {
        'global': {
            'server.socket_host': '127.0.0.1',
            'server.socket_port': 8000,
            # 'environment': production
        }
    }
    return conf


if __name__ == '__main__':
    conf = config()
    cherrypy.quickstart(Root(), '/', conf)
