import cherrypy


class Root():

    @cherrypy.expose
    def index(self, message=None):
        if message:
            return message


if __name__ == '__main__':
    cherrypy.config.update("global.cfg")
    cherrypy.quickstart(Root(), '/')
