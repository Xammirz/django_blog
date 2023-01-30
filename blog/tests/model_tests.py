from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import BlogPost, Category

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', url='test-category')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_category_ordering(self):
        category2 = Category.objects.create(name='Another Test Category', url='another-test-category')
        categories = Category.objects.all()
        self.assertEqual(list(categories), [category2, self.category])

    def test_category_verbose_name(self):
        self.assertEqual(str(Category._meta.verbose_name), 'Category')

    def test_category_verbose_name_plural(self):
        self.assertEqual(str(Category._meta.verbose_name_plural), 'Categories')


class BlogPostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Test Category', url='test-category')
        self.post = BlogPost.objects.create(author=self.user, category=self.category, title='Test Post', small_description='This is a test post.', description='This is the test post description.')

    def test_blogpost_str(self):
        self.assertEqual(str(self.post), 'Test Post')
    
    def test_blogpost_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/news/')