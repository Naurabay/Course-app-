
from courses.models import Category, Course, Contact,Branch
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from courses.serializers import CourseSerializer



class AllCourseViewTest(TestCase):
    @classmethod
    def setUp(cls):
        client = APIClient()
        contact = Contact.objects.create(choice="FACEBOOK")
        category = Category.objects.create(name="Science", imgpath="Random image")

    def test_all_course(self):
        for i in range(0,3):
            course = Course.objects.create(name="Natural science", description="??????????", logo="LOGO",
                              contact=self.contact, category=self.category)
            Branch.objects.create(latitude=str(i), longtitude=str(i), address="X-XX-XXX", course=course)
        response = client.get(reverse('All courses'))
        course_list = Course.objects.all()
        serializer = CourseSerializer(course_list, many=True)
        self.assertEquals(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)


    def new_course(self):
        courseList = {
        "name": "Chinese language school",
        "description": "Learn how to speak chinese in a month or less",
        "logo": "Some logo",
        "contact": "FACEBOOK",
        "category": "Language",
        "branches": [
            {
                "latitude": "103.5",
                "longtitude": "158.6",
                "address": "Bakery street 27"
            }
        ]
            }

        response = self.client.post(reverse("All course"), courseList, content_type="application/json")
        self.assertEquals(response.status_code, 201)
        exists = Course.objects.filter(name=response.data["Name"]).exists()
        self.assertTrue(exists)


class SingleCourseViewTest(TestCase):
    @classmethod
    def setUp(cls):
        client = APIClient()
        contact = Contact.objects.create(choice="FACEBOOK")
        category = Category.objects.create(name="Science", imgpath="image")
        course = Course.objects.create(name="First course", description="?????????????", logo="logo",
                              contact=contact, category=category)
        Branch.objects.create(latitude="53.45.3454", longtitude="4.4.4354534", address="5-45-45", course=course)

    def test_get_single_course(self):
        response = self.client.get(reverse('courses extra info', kwargs={'pk': self.course.pk}))
        course = Course.objects.get(pk=self.course.pk)
        serializer = CourseSerializer(course)
        self.assertEquals(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_delete_course(self):
        response = self.client.delete(reverse('courses extra info', kwargs={'pk': self.course.pk}))

        self.assertEquals(response.status_code, 204)
