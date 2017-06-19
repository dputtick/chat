import cherrypy


class Root():

    @cherrypy.expose
    def index(self, message=None):
        if message:
            self.add_message(message)
        messages = cherrypy.session['messages']
        return ' '.join(messages)

    def add_message(self, message):
        if not cherrypy.session.get('messages'):
            cherrypy.session['messages'] = []
        cherrypy.session['messages'].append(message)


if __name__ == '__main__':
    cherrypy.config.update('global.cfg')
    cherrypy.quickstart(Root(), '/', 'global.cfg')
