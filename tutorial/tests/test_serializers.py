from django.test import TestCase
from courses.models import Course, Category, Contact, Branch
from courses.serializers import CourseSerializer




class test_courseSerializer(TestCase):
    @classmethod
    def setUp(cls):
        contact = Contact.objects.create(choice="PHONE")
        category = Category.objects.create(name="Science", imgpath="Random image")
    def test_serializer_create_method_works(self):
        data = {
        "name": "Chemistry",
        "description": "????????????????",
        "logo": "logo",
        "contact": "PHONE",
        "category": "Science",
        "branches": [
            {
                "latitude": "40.6456",
                "longtitude": "44.4553",
                "address": "X-XX-XXX"
            }
        ]
                }
        serializer = CourseSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()

        exists = Course.objects.get(id=1)
        self.assertIsNotNone(Course.objects.get(id=1))
