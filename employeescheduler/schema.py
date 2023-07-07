import graphene
from graphene_django import DjangoObjectType #used to change Django object into a format that is readable by GraphQL
from api.models import Employee

class EmployeeType(DjangoObjectType):
    # Describe the data that is to be formatted into GraphQL fields
    class Meta:
        model = Employee
        field = ("id", "first_name", "last_name", "role", "phone_number")

class Query(graphene.ObjectType):
    #query EmployeeType to get list of employees
    list_employee=graphene.List(EmployeeType)

    def resolve_list_employee(root, info):
        # We can easily optimize query count in the resolve method
        return Employee.objects.all()

schema = graphene.Schema(query=Query)
