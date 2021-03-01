from django.test import TestCase

from course.models import Category, Course, Contact, Branch






class CourseModelTest(TestCase):
    @classmethod
    def setUpTest(cls):
        contact = Contact.objects.create(choice="EMAIL")
        category = Category.objects.create(name="Science", imgpath="Random image")
        course = Course.objects.create(name="Biology", description="?????????????", logo="Random logo", contact=contact, category=category)
        branch = Branch.objects.create(latitude="44.2445452", longtitude="34.2452345", address="ST. KV. DOM.", course=course)

    def test_category(self):
        course_category = Course.objects.get(id=1).category.name
        course_img = Course.objects.get(id=1).category.imgpath
        self.assertEquals(course_category, "Science")
        self.assertEquals(course_img, "Random image")

    def test_contact(self):
        course_contact = Course.objects.get(id=1).contact.choice
        self.assertEquals(course_contact, "EMAIL")

    def test_course(self):
        max_length = Course.objects.get(id=1)._meta.get_field("description").max_length
        course_logo = Course.objects.get(id=1).category.logo
        self.assertEquals(max_length, 500)
        self.assertEquals(course_logo, 'Random logo')


    def test_branch(self):
        branch = Branch.objects.get(id=1)
        course = Course.objects.get(id=1)
        self.assertEquals(branch.course, course)
        branch_latitude = branch.latitude
        branch_longtitude = branch.longtitude
        branch_address = branch.adress
        self.assertEquals(branch_latitude, '44.2445452')
        self.assertEquals(branch_longtitude, '34.2452345')
        self.assertEquals(branch_address, 'ST. KV. DOM.')








