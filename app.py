import web

ssl = True #activate ssl certificate 

if ssl == True:
    from web.wsgiserver import CherryPyWSGIServer
    '''
    Use OpenSSL to generate  keys

    user@host$ openssl genrsa -out server.key 1024
    user@host$ openssl req -new -key server.key -out server.csr
    user@host$ openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
    '''
    
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt" 
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key" 


urls = (
    '/', 'Index',
    '/info', 'Information',
    '/pieces', 'Pieces'
)

app = web.application(urls, globals())
render = web.template.render('templates', base='master')
web.config.debug = False        


class Index:        
    def GET(self):
        return render.index()

class Information:        
    def GET(self):
        return render.info()

class Pieces:
    """docstring for Pieces"""
    def GET(self):
        return render.pieces()
        
 
if __name__ == "__main__":
    app.run()
