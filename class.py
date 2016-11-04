class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, fname,lname, salary):
      self.fname = fname
      self.lname = lname
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
      print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.fname, " ", self.lname , "	 Salary: ", self.salary


"This would create first object of Employee class"
emp1 = Employee("Zara", "khan", 2000 )
"This would create second object of Employee class"
emp2 = Employee("Manni","mc", 5000)
emp3 = Employee("gourav", "tulsani",25000	)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print "Total Employee %d" % Employee.empCount
