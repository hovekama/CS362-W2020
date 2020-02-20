from unittest import TestCase
import classroom_manager as cm


class TestStudent(TestCase):

    def setUp(self):
        # Data setup
        self.testId = 932538626
        self.testFirst_name = "Alekos"
        self.testLast_name = "Hovekamp"

        # Initialize the Student
        self.testStudent = cm.Student(self.testId, self.testFirst_name, self.testLast_name)

    def assignmentsetUp(self):
        # Data setup for two example assignments
        self.name1 = "Assignment 4"
        self.max_score1 = 100
        self.name2 = "Assignment 5"
        self.max_score2 = 150
        self.testAssignment1 = cm.Assignment(self.name1, self.max_score1)
        self.testAssignment2 = cm.Assignment(self.name2, self.max_score2)
        self.testStudent.submit_assignment(self.testAssignment1)
        self.testStudent.submit_assignment(self.testAssignment2)

    def test_init(self):
        # Data setup
        self.setUp()

        # Perform our assertions
        self.assertEqual(self.testStudent.id, self.testId)
        self.assertEqual(self.testStudent.first_name, self.testFirst_name)
        self.assertEqual(self.testStudent.last_name, self.testLast_name)
        self.assertEqual(self.testStudent.assignments, [])

    def test_get_full_name(self):
        # Data setup
        self.setUp()

        # Perform our assertions
        self.assertEqual(self.testFirst_name + " " + self.testLast_name, self.testStudent.get_full_name())

    def test_submit_assignment(self):
        # Data setup
        self.setUp()
        self.assignmentsetUp()

        # Perform our assertions
        self.assertEqual(self.testStudent.assignments[0], self.testAssignment1)
        self.assertEqual(self.testStudent.assignments[1], self.testAssignment2)

    def test_get_assignments(self):
        # Data setup
        self.setUp()
        self.assignmentsetUp()

        # Perform our assertions
        self.assertEqual(self.testStudent.assignments, self.testStudent.get_assignments())

    def test_get_assignment(self):
        # Data setup
        self.setUp()
        self.assignmentsetUp()
        fake_name = "fake"

        # Perform our assertions
        self.assertEqual(self.testStudent.get_assignment(self.name1), self.testAssignment1)
        self.assertEqual(self.testStudent.get_assignment(fake_name), None)

    def test_get_average(self):
        # Data setup
        self.setUp()
        self.assignmentsetUp()

        # Perform our assertions
        self.assertEqual(0, self.testStudent.get_average())
        self.testStudent.assignments[0].assign_grade(90)
        self.assertEqual(45, self.testStudent.get_average())
        self.testStudent.assignments[1].assign_grade(50)
        self.assertEqual(70, self.testStudent.get_average())

    def test_remove_assignment(self):
        # Data setup
        self.setUp()
        self.assignmentsetUp()
        self.assertEqual(self.testStudent.assignments, [self.testAssignment1, self.testAssignment2])

        # Call our function once
        self.testStudent.remove_assignment(self.name1)

        # Perform our first assertion
        self.assertEqual(self.testStudent.assignments[0], self.testAssignment2)

        # Call our function once again
        self.testStudent.remove_assignment(self.name2)

        # Perform our second assertion
        self.assertEqual(self.testStudent.assignments, [])


class TestAssignment(TestCase):

    def setUp(self):
        # Data setup
        self.name1 = "Assignment 1"
        self.max_score1 = 200
        self.testAssignment = cm.Assignment(self.name1, self.max_score1)

    def test_init(self):
        # Data setup
        self.setUp()

        # Perform our assertions
        self.assertEqual(self.testAssignment.name, self.name1)
        self.assertEqual(self.testAssignment.max_score, self.max_score1)
        self.assertEqual(self.testAssignment.grade, None)


    def test_assign_grade(self):
        # Data setup
        self.setUp()
        grade_big = 300
        grade_ok = 100

        # Call our function once
        self.testAssignment.assign_grade(grade_big)

        # Perform our assertion once to test the branch where
        # the grade is larger than the max score
        self.assertEqual(self.testAssignment.grade, None)

        # Call our function the second time with an ok grade
        self.testAssignment.assign_grade(grade_ok)

        # Perform our final assertion
        self.assertEqual(self.testAssignment.grade, grade_ok)

