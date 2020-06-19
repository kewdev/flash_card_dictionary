from time import sleep

from selenium import webdriver
import unittest

# TODO: создать тесты регистрации пользователя (или только формы регистрации)
# TODO: создать тесты создания групп (на странице с детализацией
#  группы должны содержатся слова, принаждежащие этой группе) и  добавлени групп к словам
# TODO: создать тесты создания языков (на странице с детализацией
#  языка должны содержатся слова, принаждежащие этому языку)
# TODO: создать тесты для поиска слов
# TODO: создать тесты создания наборов слов для повторения
from selenium.common.exceptions import NoSuchElementException


class NewVisitorTest(unittest.TestCase):
    '''Тест нового посетителя'''

    def setUp(self) -> None:
        self.site_url = 'http://127.0.0.1:8000/'
        self.test_user_name = 'testuser'
        self.test_user_pass = '1234'
        self.browser = webdriver.Firefox()
        self.first_word = 'run'
        self.first_translation = 'бежать, запускать'
        self.second_word = 'apple'
        self.second_translation = 'яблоко'

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_dictionary_and_retrieve_it_later(self):
        # зарегистрированный пользователь заходит на сайт

        self.browser.get('http://127.0.0.1:8000/instructions/')

        # видит в заголовке название сайта которое говорит о словарях

        self.assertIn('слов', self.browser.title) # TODO: регистронезависимая проверка

        ############################################################### пользователь хочет начать свой словарь и видит инструкцию которая говорит, что нужно:
        ###############################################################   - зарегистрироваться на сайте или войти с помощью соц. сети
        ###############################################################   - задать язык, на котором будет вестись словарь
        ###############################################################   - начать добавлять слова в словарик

        # пользователь видит кнопки "Вход" и "Регистрация" в шапке сайта

        self.assertIn('Вход', self.browser.find_element_by_id("login").text)
        self.assertIn('Регистрация', self.browser.find_element_by_id("signup").text)

        # он нажимает на кнопку "Вход"

        self.browser.find_element_by_id('login').click()

        # и переходит на страницу входа,
        # на странице входа он видит поля ввода для логина и пароля,
        # а так же кнопку входа с помощью соц. сети vk TODO

        user_name_field = self.browser.find_element_by_id('id_login')
        user_pass_field = self.browser.find_element_by_id('id_password')

        # пользователь вводит свой логин, пароль и нажимет кнопку войти

        user_name_field.send_keys(self.test_user_name)
        user_pass_field.send_keys(self.test_user_pass)
        self.browser.find_element_by_class_name('primaryAction').click()

        # пользователя перенаправляет на главную страницу создания слов

        self.assertEqual(self.site_url + 'word/', self.browser.current_url)

        # теперь в шапке сайта нет кнопок "Вход" и "Регистрация"

        with self.assertRaises(NoSuchElementException) as context:
            self.browser.find_element_by_id("login")
        with self.assertRaises(NoSuchElementException) as context:
            self.browser.find_element_by_id("signup")

        # вместо них он видит своё имя и кнопку "Выход",

        self.assertIn(self.test_user_name, self.browser.find_element_by_id('user_name').text)
        self.assertIn('Выход', self.browser.find_element_by_id('logout').text)

        # Пользователль создаёт слово

        self.browser.find_element_by_id('add_new_word').click()

        # перенаправляется на страницу добавления слова

        self.assertEqual(self.site_url + 'word/create/', self.browser.current_url)

        # вводит слово

        self.browser.find_element_by_id('id_word').send_keys(self.first_word)

        # вводит перевод

        self.browser.find_element_by_id('id_translation').send_keys(self.first_translation)

        # нажимает кнопку save

        self.browser.find_element_by_id('save_button').click()

        # перенаправляетвся на страницу с деталями слова

        self.assertIn(self.site_url + 'word/detail/', self.browser.current_url)
        self.assertNotEqual(self.site_url + 'word/detail/', self.browser.current_url)

        # добаляет ещё одно слово: видит кнопку добавления слова, нажимает на неё

        self.browser.find_element_by_id('add_new_word').click()

        # перенаправляется на страницу добавления слова

        self.assertEqual(self.site_url + 'word/create/', self.browser.current_url)

        # вводит слово
        self.browser.find_element_by_id('id_word').send_keys(self.second_word)

        # вводит перевод

        self.browser.find_element_by_id('id_translation').send_keys(self.second_translation)

        # нажимает кнопку save

        self.browser.find_element_by_id('save_button').click()

        # перенаправляетвся на страницу с детальнями слова

        self.assertIn(self.site_url + 'word/detail/', self.browser.current_url)
        self.assertNotEqual(self.site_url + 'word/detail/', self.browser.current_url)

        # пользователь проверяет, сохранились ли его слова на сайте:
        #   нажимает на кнопку-логотип

        logo = self.browser.find_element_by_id('logo')

        # которая ведёт в корень сайта "/"

        self.assertEqual(logo.get_attribute('href'), self.site_url)
        logo.click()

        # перенаправляется на сраницу со списком слов "/word/"

        self.assertIn(self.site_url + 'word/', self.browser.current_url)

        # видит слова

        card_headers = self.browser.find_elements_by_css_selector('.card-header a h4')
        self.assertTrue(
            any(card_header.text == self.first_word for card_header in card_headers)
        )
        self.assertTrue(
            any(card_header.text == self.second_word for card_header in card_headers)
        )

        card_bodys = self.browser.find_elements_by_css_selector('.card-body p')
        self.assertTrue(
            any(card_body.text == self.first_translation for card_body in card_bodys)
        )
        self.assertTrue(
            any(card_body.text == self.second_translation for card_body in card_bodys)
        )

        # пользователь делает logout
        # нажимает на кнопку "Выйти"

        self.browser.find_element_by_id('logout').click()
        sleep(1)

        # перенаправляется на страницу выход из сайта

        self.assertEqual(self.site_url + 'accounts/logout/', self.browser.current_url)

        # нажимает на кнопку выйти

        self.browser.find_element_by_id('logout_button').click()

        # перенаправляется на на индекс-страницу

        self.assertEqual(self.site_url + 'instructions/', self.browser.current_url)

        # пользователь нажимает на лого

        self.browser.find_element_by_id('logo').click()

        # и его перенаправляет на индекс-страницу

        self.assertEqual(self.site_url + 'instructions/', self.browser.current_url)

        # пользователь делает login
        # он нажимает на кнопку "Вход"

        self.browser.find_element_by_id('login').click()

        # перенаправляется на страницу входа
        self.assertEqual(self.browser.current_url, self.site_url + 'accounts/login/')

        # пользователь вводит свой логин, пароль и нажимет кнопку войти

        user_name_field = self.browser.find_element_by_id('id_login')
        user_pass_field = self.browser.find_element_by_id('id_password')

        user_name_field.send_keys(self.test_user_name)
        user_pass_field.send_keys(self.test_user_pass)
        self.browser.find_element_by_class_name('primaryAction').click()

        # перенаправляется на страницу со словами

        self.assertEqual(self.browser.current_url, self.site_url + 'word/')

        # видит, что его слова остались неизменными

        card_headers = self.browser.find_elements_by_css_selector('.card-header a h4')
        self.assertTrue(
            any(card_header.text == self.first_word for card_header in card_headers)
        )
        self.assertTrue(
            any(card_header.text == self.second_word for card_header in card_headers)
        )

        card_bodys = self.browser.find_elements_by_css_selector('.card-body p')
        self.assertTrue(
            any(card_body.text == self.first_translation for card_body in card_bodys)
        )
        self.assertTrue(
            any(card_body.text == self.second_translation for card_body in card_bodys)
        )


if __name__ == '__main__':
    unittest.main(warnings='ignore')
