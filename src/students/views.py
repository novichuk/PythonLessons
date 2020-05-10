from django.http import HttpResponse
import random
import string
from students.models import Student #Import model

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

    #http://127.0.0.1:8000/hello-world/?lenght=10

    return HttpResponse(
        generate_password(
            int(request.GET['lenght'])
        )
    )



def students(request):
    count = Student.objects.count() #SELECT COUNT(*) FROM students_student;
    students_queryset = Student.objects.all() #SELECT * FROM students_student; #QuerySet

    response = f'students: {count}<br/>'

    for student in students_queryset:
        # print(student.id, student.first_name)
        # print(student.full_name)
        # print(student.info())
        response += student.info() + '<br/>'

    return HttpResponse(response)

