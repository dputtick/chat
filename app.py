import cherrypy


class Root():

    @cherrypy.expose
    def index(self, message=None):
        if message:
            if not cherrypy.session.get('messages'):
                cherrypy.session['messages'] = []
            cherrypy.session['messages'].append(message)
        messages = cherrypy.session['messages']
        retlist = [m + '\n' for m in messages[:-1]]
        retlist.append(messages[-1])
        return ''.join(retlist)

    def add_message(message):
        pass


if __name__ == '__main__':
    cherrypy.config.update("global.cfg")
    cherrypy.quickstart(Root(), '/')
