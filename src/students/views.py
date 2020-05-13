import random
import string

from django.http import HttpResponse

from faker import Faker

from students.models import Student


def generate_password(lenght: int = 10) -> str:
    choices = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(lenght):
        password += random.choice(choices)
    return password


def hello_world(request):
    # print(request)
    # print('request.GET')
    # print(request.GET)
    # breakpoint()
    # pdb.set_trace()
    # return HttpResponse('hello')

    # http://127.0.0.1:8000/hello-world/?lenght=10

    return HttpResponse(
        generate_password(
            int(request.GET['lenght'])
        )
    )


def students(request):
    count = Student.objects.count()  # SELECT COUNT(*) FROM students_student;
    students_queryset = Student.objects.all()  # SELECT * FROM students_student; #QuerySet

    response = f'students: {count}<br/>'

    for student in students_queryset:
        # print(student.id, student.first_name)
        # print(student.full_name)
        # print(student.info())
        response += student.info() + '<br/>'

    return HttpResponse(response)


def generate_student(request):  # 1 student generator
    fake = Faker()

    student = Student.objects.create(first_name=fake.first_name(),
                                     last_name=fake.last_name(),
                                     age=random.randrange(17, 65),
                                     )
    response = f'New student created: {student.info()}'
    return HttpResponse(response)


def students_generator(count: int = 1):  # 1 or more students generator
    # try:
    #     count = int(request.GET['count'])
    # except:
    #     pass

    all_responses = ''
    fake = Faker()

    for i in range(int(count)):
        student = Student.objects.create(first_name=fake.first_name(),
                                         last_name=fake.last_name(),
                                         age=random.randrange(17, 65),
                                         )
        response = f'New student created: {student.info()}'
        all_responses += response
    return HttpResponse(all_responses)


def generate_students(request):
    count = request.GET['count']
    response = ''

    if count.isdigit() and int(count) > 0:
        print('hi')
        response = HttpResponse(students_generator(int(count)))
    else:
        response = 'Please enter amount of students 1 or more'

    return HttpResponse(response)
