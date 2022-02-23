from importlib.resources import path
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from todo.models import UserModel


class TestHomePage(TestCase):
    def setUp(self) -> None:
        return super().setUp()
        self.client = Client
        
    def tearDown(self) -> None:
        return super().tearDown()

    def test_home_page_status_200(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_home_page_text(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.content.decode('utf-8'), 'welcome')   

class TestTodoModels(TestCase):
    def setUp(self) -> None:
        self.user_data = {
            'username': 'test1',
            'first_name': 'test',
            'last_name': 'one',
            'email': 'test1@email.com',
            'password': 'test@1'
        }
        self.client = Client()        
        return super().setUp()
                
        
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_no_users_initially(self):        
        self.assertEqual(UserModel.objects.all().count(), 0)

    def test_create_user_manually(self):        
        obj = UserModel.objects.create(**self.user_data)
        self.assertEqual(UserModel.objects.all().count(), 1)
    
    def test_signup_302(self):                        
        resp = self.client.post(path=reverse('todo:sign-up'), data=self.user_data)        
        self.assertEqual(resp.status_code, 302)
    
    def test_create_user_on_signup(self):                        
        resp = self.client.post(path=reverse('todo:sign-up'), data=self.user_data)        
        self.assertEqual(UserModel.objects.count(), 1)
    
    def test_check_user_created_user_data(self):                        
        resp = self.client.post(path=reverse('todo:sign-up'), data=self.user_data)        
        self.assertEqual(UserModel.objects.all()[0].username, self.user_data['username'])

class TestTodoUrls(TestCase):
    def setUp(self) -> None:
        self.user_data = {
            'username': 'test1',
            'first_name': 'test',
            'last_name': 'one',
            'email': 'test1@email.com',
            'password': 'test@1'
        }
        self.client = Client()        
        return super().setUp()
                        
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_todo_home_page_url(self):
        resp = self.client.get(reverse('todo:todo-home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_todo_signup_url_get(self):
        resp = self.client.get(reverse('todo:sign-up'))
        self.assertEqual(resp.status_code, 200)    
    
    def test_todo_login_url_get(self):
        resp = self.client.get(reverse('todo:login'))
        self.assertEqual(resp.status_code, 200)    
        
    def test_todo_dashboard(self):
        resp = self.client.get(reverse('todo:dashboard'))
        # if not authenticated user won't be able to see 302, and redirected to todo-home
        self.assertEqual(resp.status_code, 302)            
    
    def test_todo_login_url_post_invalid_username(self):        
        resp = self.client.post(path=reverse('todo:login'), data={'username':'test1', 'password': 'test@1'})        
        self.assertEqual(resp.status_code, 400)    
        self.assertTrue('invalid user' in resp.content.decode('utf-8'))
    
    def test_todo_login_url_post_invalid_password(self):
        obj = UserModel.objects.create(**self.user_data)
        resp = self.client.post(path=reverse('todo:login'), data={'username':'test1', 'password': 'test@2'})        
        self.assertEqual(resp.status_code, 400)    
        self.assertTrue('wrong password' in resp.content.decode('utf-8'))
