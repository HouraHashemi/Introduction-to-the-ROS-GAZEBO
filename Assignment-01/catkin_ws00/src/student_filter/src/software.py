#!/usr/bin/python

from student_filter.msg import Student
from random import randint, seed, choice
from time import time
import rospy


def callback(data):
    rospy.loginfo("S\n------------------------------\nStudent Info:\n\t Name: {}\n \
        LastName: {}\n\t Age: {}\n\t Departement: {}\n------------------------------\n"
        .format(data.name, data.last_name, data.age, data.departement))       


def listener():
    student = Student()
    rospy.init_node('software', anonymous=True)
    rospy.Subscriber('software',Student, callback)

    rospy.spin()
    rate = rospy.Rate(1)


if __name__ == '__main__':
    listener()
    