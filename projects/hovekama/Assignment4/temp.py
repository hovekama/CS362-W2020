def setUp(self):
    # Data setup
    self.id = 932538626
    self.first_name = "Alekos"
    self.last_name = "Hovekamp"

    # Initialize the Student
    self.testStudent = cm.Student(self.id, self.first_name, self.last_name)


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
    self.assertEqual(self.testStudent.id, self.id)
    self.assertEqual(self.testStudent.first_name, self.first_name)
    self.assertEqual(self.testStudent.last_name, self.last_name)
    self.assertEqual(self.testStudent.assignments, [])


def test_get_full_name(self):
    # Data setup
    self.setUp()

    # Perform our assertions
    self.assertEqual(self.first_name + " " + self.last_name, self.testStudent.get_full_name())


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
    self.assertEqual(-1, self.testStudent.get_average())
    self.testStudent.assignments[0].assign_grade(90)
    self.assertEqual(90, self.testStudent.get_average())
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
    self.assertEqual(self.testStudent.assignments, [self.testAssignment2])

    # Call our function once again
    self.testStudent.remove_assignment(self.name2)

    # Perform our second assertion
    self.assertEqual(self.testStudent.assignments, [])