IP = "67.205.147.14"
DIR := ${CURDIR}
USER = "cherrypy"
REMDIR = "/home/cherrypy/cherry-chat"


rsync python:
	rsync -avz -e "ssh" --progress $(DIR)/*.py $(USER)@$(IP):$(REMDIR)
