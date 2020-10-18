from rest_framework import serializers
from .models import Category, Course, Branch,Contact

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"


class BranchSerializer(serializers.Serializer):
    class Meta:
        model = Branch
        fields =["latitude", "longtitude", "adress"]


class ContactSerializer(serializers.Serializer):
    class Meta:
        model = Contact
        fields = ["contact_type","value"]


class CourseSerializer(serializers.ModelSerializer):
    # contacts = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all(CONTACTS))
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
           model = Course
           fields = (

               "name",
               "description",
               "category",
               "logo",
               "contacts",
               "branches",
           )



    def create(self, validated_data):

            contact = validated_data.pop('contacts')
            branch = validated_data.pop('branches')

            course = Course.objects.create(**validated_data)


            Contact.objects.create(course=course, **contact)

            Branch.objects.create(course=course, **branch)
            return course

