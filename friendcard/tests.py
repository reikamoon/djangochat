from django.test import TestCase
from friendcard.models import FriendCard
from django.contrib.auth.models import User

# Create your tests here.
class FriendCardTestCase(TestCase):
    def test_true_is_true(self):
        self.assertEqual(True, True)

    def test_create_card(self):
        user = User()
        user.save()

        # Create and save a new page to the test database.
        card = FriendCard(name = "Test Person", author = user, created = "2020-02-20", nickname = "Test", gender = "test", birthday = "2020-03-05", home = "Heroku", email = "email@email.com", bio = "I'm a test.")
        card.save()

        self.assertEqual(card.name, "Test Person")

    def test_gender_name(self):
        user = User()
        user.save()

        # Create and save a new page to the test database.
        card = FriendCard(name = "Test Person", author = user, created = "2020-02-20", nickname = "Test", gender = "test", birthday = "2020-03-05", home = "Heroku", email = "email@email.com", bio = "I'm a test.")
        card.save()

        self.assertEqual(card.gender, "test")

class CardListViewTests(TestCase):
    def test_multiple_cards(self):
        # Make some test data to be displayed on the page.
        user = User.objects.create()

        FriendCard.objects.create(name = "Test Person", author = user, created = "2020-02-20", nickname = "Test", gender = "test", birthday = "2020-03-05", home = "Heroku", email = "email@email.com", bio = "I'm a test.")
        FriendCard.objects.create(name = "Test Person2", author = user, created = "2020-02-20", nickname = "Test", gender = "test", birthday = "2020-03-05", home = "Heroku", email = "email@email.com", bio = "I'm a test.")

        # When we make a request, we get a response back.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template
        # matches the number of pages we have in the database.
        responses = response.context['cards']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<FriendCard: Test Person>', '<FriendCard: Test Person2>'],
            ordered=False
        )
