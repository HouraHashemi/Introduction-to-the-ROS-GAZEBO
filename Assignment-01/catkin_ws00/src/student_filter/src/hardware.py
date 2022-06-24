#!/usr/bin/python
#!/usr/bin/python
 
from student_filter.msg import Student
from random import randint, seed, choice
from time import time
import rospy


def callback(data):
    rospy.loginfo("H\n------------------------------\nStudent Info:\n\t Name: {}\n\t LastName: {}\n \
        Age: {}\n\t Departement: {}\n------------------------------\n"\
        .format(data.name, data.last_name, data.age, data.departement))       


def listener():
    student = Student()
    rospy.init_node('hardware', anonymous=True)
    rospy.Subscriber('hardware',Student, callback)

    rospy.spin()
    rate = rospy.Rate(1)


if __name__ == '__main__':
    listener()