import web
import re
from Models import RegisterModel, LoginModel, Posts, Experience
import psycopg2
import os
import sys
import simplejson

web.config.debug = False

urls = (
    '/', 'home',
    '/register', 'register',
    '/postregisteration', 'postregisteration',
    '/login', 'Login',
    '/logout', 'Logout',
    '/checklogin', 'Checklogin',
    '/postactivie', 'PostActivity',
    '/postexper', 'PostExper',
    '/profile/(.*)/info', 'UserInfo',
    '/profile/(.*)', 'UserProfile',  # send the user name from the profile page
    '/settings', 'Settings',
    '/update-settings', 'Updatesettings',
    '/comment-activity', 'Submitcomment',
    '/deletepost', 'Deletepost',
    '/upload-image/(.*)', 'UploadImage'
)

app = web.application(urls, globals())

session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'user': None})

session_data = session.initializer

render = web.template.render('Views/templates', base="main-layout",
                             globals={'session': session_data, 'current_user': session_data['user']})
render2 = web.template.render('Views/templates', base="html-tem",
                              globals={'session': session_data, 'current_user': session_data['user']})


class home:
    def GET(self):
        post_model = Posts.Posts()
        posts = post_model.get_all_posts()
        return render.home(posts)


class register:
    def GET(self):  # get is for url
        return render.register()


class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']
        post_model = Posts.Posts()
        post_model.inser_post(data)

        return 'success'


class PostExper:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']
        exper_model = Experience.Experience()
        exper_model.inser_exper(data)

        return 'success'


class Login:
    def GET(self):
        return render.login()


class UserProfile:
    def GET(self, user):
        login = LoginModel.LoginModel()
        user_info = login.get_profile(user)

        post_model = Posts.Posts()
        posts = post_model.get_all_posts()
        return render.profile(render2.fecth_post(posts, user_info))


class UserInfo:
    def GET(self, user):
        login = LoginModel.LoginModel()
        user_info = login.get_profile(user)

        exper_model = Experience.Experience()
        expers = exper_model.get_all_expers()
        return render.profile(render2.info(user_info, expers))


class Settings:
    def GET(self):
        return render.profile(render2.setting())


class Updatesettings:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        settings_model = LoginModel.LoginModel()
        if settings_model.update_info(data):
            return 'success'
        else:
            return 'Error'


class Submitcomment:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        comment_model = Posts.Posts()
        added_comment = comment_model.add_comment(data)

        if added_comment:
            return added_comment
        else:
            return 'Error'


class Deletepost:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        delete_model = Posts.Posts()
        delete_post = delete_model.delete_post(data)

        if delete_post:
            return 'success'
        else:
            return 'Error'


class postregisteration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)

        return data.username


class Checklogin:
    def POST(self):
        data = web.input()
        login_model = LoginModel.LoginModel()
        isCorrect = login_model.check_user(data)

        if isCorrect:
            session_data['user'] = isCorrect
            return isCorrect

        return 'error'


class Logout:
    def GET(self):
        session['user'] == None
        session_data == None
        session.kill()
        if session['user'] == None:
            return 'success'
        else:
            return 'something wrong'


class UploadImage:
    def POST(self, type):  # image or bg
        file = web.input(avatar={}, background={})
        file_dir = os.getcwd() + "/static/upload/" + session_data['user']['username']

        if not os.path.exists(file_dir):
            os.mkdir(file_dir)

        if 'avatar' or 'background' in file:
            filepath = file[type].filename.replace("\\", "/")
            filename = filepath.split('/')[-1]
            f = open(file_dir + '/' + filename, 'wb')
            f.write(file[type].file.read())
            f.close()

            update = {}
            update['type'] = type
            update['img'] = '/static/upload/' + session_data['user']['username'] + '/' + filename
            update['username'] = session_data['user']['username']

            account_model = LoginModel.LoginModel()
            update_avater = account_model.update_image(update)

        raise web.seeother('/settings')  # redirect


if __name__ == "__main__":
    app.run()
