import web

# URLs?
urls = ("/(.*)/(.*)", "index")
render = web.template.render("resources/")
app = web.application(urls, globals())


class index:
    def GET(self, name, age):
        return render.main(name, age)

# __?
if __name__ == "__main__":
    app.run()
