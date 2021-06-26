from django.test import TestCase
from InstaPy.instapy import InstaPy

# Create your tests here.


user_pass_list = [{'username': 'homovej284', 'password': '94703@Qqq'},
                  {'username': 'homovej284', 'password': '94703@Qqq'},
                  ]

my_follow_list = ['mr_6804', 'coffee.in.home']


def login(username, password, nogui):
    instagram = InstaPy(username=username, password=password,
                        nogui=nogui,
                        geckodriver_path='/home/mohammad/driver/geckodriver')
    instagram.login()

    return instagram


def follow_by_list(instagram, follow_list):
    # instagram = InstaPy(geckodriver_path = '/home/mohammad/driver/geckodriver')
    instagram.follow_by_list(follow_list)


# login(user_pass_list[0]['password'], user_pass_list[0]['password'])

class MyInstagramBot(TestCase):

    # def test_login(self):
    #     login(user_pass_list[1]['username'], user_pass_list[1]['password'], True)

    # def test_follow(self):
    #     instagram = login(user_pass_list[1]['username'], user_pass_list[1]['password'], False)
    #     follow_by_list(instagram, my_follow_list)

    def test_like(self):
        instagram = login(user_pass_list[1]['username'], user_pass_list[1]['password'], False)
        # follow_by_list(instagram, my_follow_list)
        # instagram.set_do_like(True, percentage=10)
        # instagram.interact_by_users(['mr_6804'], amount=1)
        # instagram.end()

