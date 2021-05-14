import web

# URLs?
urls = ("/", "home")
render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(urls, globals())


# Classes and Routes
class home:
    def GET(self):
        return render.Home()


# __?
if __name__ == "__main__":
    app.run()
