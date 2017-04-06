import web
        
urls = (
    '/', 'Index',
    '/info', 'Information',
    '/contact', 'Contact',
    '/about', 'About',
    '/login', 'Login',
    '/signup', 'Signup'
)

app = web.application(urls, globals())
render = web.template.render('templates', base='master')
"""renderIndex = web.template.render('templates', base='masterIndex')"""
web.config.debug = False

class Index:        
    def GET(self):
        return render.index()

class Information:        
    def GET(self):
        return render.info()

class Contact:        
    def GET(self):
        return render.contact()

class About:        
    def GET(self):
        return render.about()

class Login:        
    def GET(self):
        return render.login()

class Signup:        
    def GET(self):
        return render.signup()
 
if __name__ == "__main__":
    app.run()
