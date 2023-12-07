from rest_framework import serializers

from my_app.models import User, Student, Course


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', )

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()

        return user


class RelatedCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', )


class RelatedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class StudentSerializer(serializers.ModelSerializer):
    courses = RelatedCourseSerializer(
        many=True,
        read_only=True
    )
    # user = RelatedUserSerializer()
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Student
        fields = ('id', 'user', 'courses')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
