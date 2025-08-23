from django.test import TestCase
from .models import Task, Author
from django.utils import timezone

# Create your tests here.
class TaskModelTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Charles Obiero",
        email = "charles@gmail.com")

    def test_task_str(self):
        task = Task (
            title = "Write tests", 
            description = 'Ensuring all model attributes have correct tests',
            due_date = timezone.now().date(),
            author = self.author, 
        )

        expected_str = "Title: Write tests\n\nDescription: Ensuring all model attributes have correct tests"

        self.assertEqual(str(task), expected_str)
