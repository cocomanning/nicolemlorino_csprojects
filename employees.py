"""
I coded the following program with my class partner, Maryam Elbeltagy, for CS 313E at
the University of Texas at Austin.

This program simulates a model of the worst company, in which an employee's mood and 
well-being varies with the simulated work environment and coworker relationships.
"""

from abc import ABC, abstractmethod
import random

DAILY_EXPENSE = 60
HAPPINESS_THRESHOLD = 50
MANAGER_BONUS = 1000
TEMP_EMPLOYEE_PERFORMANCE_THRESHOLD = 50
PERM_EMPLOYEE_PERFORMANCE_THRESHOLD = 25
RELATIONSHIP_THRESHOLD = 10
INITIAL_PERFORMANCE = 75
INITIAL_HAPPINESS = 50
PERCENTAGE_MAX = 100
PERCENTAGE_MIN = 0
SALARY_ERROR_MESSAGE = "Salary must be non-negative."


class Employee(ABC):
    """
    Abstract base class representing a generic employee in the system.
    """

    def __init__(self, name, manager, salary, savings):
        self.relationships = {}
        self.savings = savings
        self.is_employed = True
        self.__name = name
        self.__manager = manager
        self.performance = INITIAL_PERFORMANCE
        self.happiness = INITIAL_HAPPINESS
        self.salary = salary

    @property
    def name(self):
        """returns employee name"""
        return self.__name
    @property
    def manager(self):
        """returns employee manager"""
        return self.__manager
    @property
    def performance(self):
        """returns employee performance"""
        return self.__performance
    @performance.setter
    def performance(self, new_performance):
        self.__performance = new_performance
        if new_performance < PERCENTAGE_MIN:
            self.__performance = PERCENTAGE_MIN
        if new_performance > PERCENTAGE_MAX:
            self.__performance = PERCENTAGE_MAX

    @property
    def happiness(self):
        """returns employee happiness"""
        return self.__happiness
    @happiness.setter
    def happiness(self, new_happiness):
        self.__happiness = new_happiness
        if new_happiness < PERCENTAGE_MIN:
            self.__happiness = PERCENTAGE_MIN
        if new_happiness > PERCENTAGE_MAX:
            self.__happiness = PERCENTAGE_MAX

    @property
    def salary(self):
        """returns employee salary"""
        return self.__salary
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError(SALARY_ERROR_MESSAGE)
        self.__salary = new_salary

    @abstractmethod
    def work(self):
        """will be implemented by subclasses"""

    def interact(self, other):
        """interaction between employees"""
        if other.name not in self.relationships:
            self.relationships[other.name] = 0
        if self.relationships[other.name] > RELATIONSHIP_THRESHOLD:
            self.happiness += 1
        elif self.__happiness >= HAPPINESS_THRESHOLD and other.happiness >= HAPPINESS_THRESHOLD:
            self.relationships[other.name] += 1
        else:
            self.relationships[other.name] -= 1
            self.happiness -= 1

    def daily_expense(self):
        """daily expense of each day"""
        self.happiness -= 1
        self.savings -= DAILY_EXPENSE

    def __str__(self):
        return (f"{self.name}\n"
                f"\tSalary: ${self.salary}\n"
                f"\tSavings: ${self.savings}\n"
                f"\tHappiness: {self.happiness}%\n"
                f"\tPerformance: {self.performance}%")


class Manager(Employee):
    """
    A subclass of Employee representing a manager.
    """

    def work(self):
        new_performance = random.randint(-5,5)
        self.performance += new_performance

        if new_performance <= 0:
            self.happiness -=1
            for relationship, score in self.relationships.items():
                self.relationships[relationship] = score - 1
        elif new_performance > 0:
            self.happiness += 1

class TemporaryEmployee(Employee):
    """
    A subclass of Employee representing a temporary employee.
    """

    def work(self):
        new_performance = random.randint(-15,15)
        self.performance += new_performance
        if new_performance > 0:
            self.happiness += 1
        else:
            self.happiness -= 2
    def interact(self, other):
        Employee.interact(self, other)
        if self.manager == other:
            if other.happiness > HAPPINESS_THRESHOLD:
                if self.performance >= TEMP_EMPLOYEE_PERFORMANCE_THRESHOLD:
                    self.savings += MANAGER_BONUS
            elif other.happiness <= HAPPINESS_THRESHOLD:
                self.salary = self.salary // 2
                self.happiness -= 5
                if self.salary <= 0:
                    self.is_employed = False

class PermanentEmployee(Employee):
    """
    A subclass of Employee representing a permanent employee.
    """

    def work(self):
        new_performance = random.randint(-10,10)
        self.performance += new_performance
        if new_performance >=0:
            self.happiness += 1
    def interact(self, other):
        Employee.interact(self, other)
        if self.manager == other:
            if other.happiness > HAPPINESS_THRESHOLD:
                if self.performance >= PERM_EMPLOYEE_PERFORMANCE_THRESHOLD:
                    self.savings += MANAGER_BONUS
            elif other.happiness <= HAPPINESS_THRESHOLD:
                self.happiness -= 1
