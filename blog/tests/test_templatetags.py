from django.test import TestCase
from django.contrib.auth import get_user_model

from blog.templatetags.blog_extras import author_details


class AuthorDetailsTests(TestCase):

    def test_author_has_first_and_last_name(self):
        User = get_user_model()
        author = User(first_name="John", last_name="Doe", email="john.doe@example.com")
        current_user = User(first_name="Jane", last_name="Doe")
        expected_output = '<a href="mailto:john.doe@example.com">John Doe</a>'
        self.assertEqual(author_details(author, current_user), expected_output)

    def test_author_has_only_username(self):
        User = get_user_model()
        author = User(username="john_doe")
        current_user = User(first_name="Jane", last_name="Doe")
        expected_output = 'john_doe'
        self.assertEqual(author_details(author, current_user), expected_output)

    def test_author_is_current_user(self):
        User = get_user_model()
        author = User(first_name="Jane", last_name="Doe")
        current_user = author
        expected_output = '<strong>me</strong>'
        self.assertEqual(author_details(author, current_user), expected_output)

    def test_author_has_no_email(self):
        User = get_user_model()
        author = User(first_name="John", last_name="Doe")
        current_user = User(first_name="Jane", last_name="Doe")
        expected_output = 'John Doe'
        self.assertEqual(author_details(author, current_user), expected_output)

    def test_author_is_not_user_object(self):
        User = get_user_model()
        author = "not a user"
        current_user = User(first_name="Jane", last_name="Doe")
        expected_output = ''
        self.assertEqual(author_details(author, current_user), expected_output)
