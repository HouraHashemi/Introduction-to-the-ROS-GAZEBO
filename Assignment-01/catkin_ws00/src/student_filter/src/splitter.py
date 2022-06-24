#!/usr/bin/python

from student_filter.msg import Student
from random import randint, seed, choice
from time import time
import rospy


def callback(data):
    rospy.loginfo("RECEIVE DATA:\n\t Name: {}, Last_name: {}, Age: {}, Departement: {}\n"\
            .format(data.name, data.last_name, data.age, data.departement))

def check_departement(data):
    pub_s = rospy.Publisher('software', Student, queue_size=10)
    pub_h = rospy.Publisher('hardware', Student, queue_size=10)

    if data.departement == "Software":
        pub_s.publish(data)
    elif  data.departement == "Hardware":
        pub_h.publish(data)
    else:
        rospy.loginfo("Invalid Data!")


def listener():
    student = Student()
    rospy.init_node('splitter', anonymous=True)
    rospy.Subscriber('std_request',Student, callback)
    rospy.Subscriber('std_request',Student, check_departement)

    rospy.spin()
    # rate = rospy.Rate(1)


if __name__ == '__main__':
    listener()