from django.test import TestCase
from .forms import CollaborateForm


def test_form_is_valid1(self):
    """ Test for all fields"""
    form = NewCookbookForm({
        'title': 'Grandmas Finest' ,
        'cover_image': '' ,
        'description': 'Secret Recipes' ,
        'status': '1' ,
        'excerpt': 'Secrets'  })
    self.assertTrue(form.is_valid(), msg="Form is not valid")


def test_form_is_valid2(self):
    """ Test for all fields"""
    form = NewDishForm({
        'title': 'Porridge' ,
        'featured_image': '' ,
        'content': 'Tasty Oat Soup' ,
        'ingredients': 'oats, milk, salt' ,
        'status': '1' ,
        'excerpt': 'Tasty' ,
        'category': '7' ,
        'prep_time_minutes': '5' ,
        'prep_time_hours': '' ,
        'cook_time_minutes': '12' ,
        'cook_time_hours': ''  })
    self.assertTrue(form.is_valid(), msg="Form is not valid")


def test_form_is_valid3(self):
    """ Test for all fields"""
    form = ChefProfileForm({
        'bio': 'I am a chef' ,
        'location': 'Chef-town' ,
        'birth_date': '21/12/1990' ,
        'profile_pic': '' ,
        'facebook_url': 'facebook.com' ,
        'twitter_url': 'twitter.com' ,
        'instagram_url': 'instagram.com' ,
        'pinterest_url': 'pinterest.com' ,
        'tiktok_url': 'tiktok.com' ,
        'website_url': 'github.com' })
    self.assertTrue(form.is_valid(), msg="Form is not valid")


def test_form_is_valid4(self):
    """ Test for all fields"""
    form = CollaborateForm({
        'name': 'jo',
        'email': 'test@test.com',
        'message': 'Hello!'
    })
    self.assertTrue(form.is_valid(), msg="Form is not valid")


def test_name_is_required(self):
    """Test for the 'name' field"""
    form = CollaborateForm({
        'name': '',
        'email': 'test@test.com',
        'message': 'Hello!'
    })
    self.assertFalse(
        form.is_valid(),
        msg="Name was not provided, but the form is valid"
    )

def test_email_is_required(self):
    """Test for the 'email' field"""
    form = CollaborateForm({
        'name': 'Matt',
        'email': '',
        'message': 'Hello!'
    })
    self.assertFalse(
        form.is_valid(),
        msg="Email was not provided, but the form is valid"
    )

def test_message_is_required(self):
    """Test for the 'message' field"""
    form = CollaborateForm({
        'name': 'Matt',
        'email': 'test@test.com',
        'message': ''
    })
    self.assertFalse(
        form.is_valid(),
        msg="Message was not provided, but the form is valid"
    )