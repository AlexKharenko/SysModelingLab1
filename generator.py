import math
import random 


class NumberGenerator:
    def __init__(self):
        self.dispersion =0
        self.average =0
        self.numbers = []

    def _emptyNumbers(self):
        if not self.numbers:
            raise Exception('Numbers array is empty!')

    def SolveAverage(self):
        self._emptyNumbers()
        sum = 0
        for i in range(len(self.numbers)):
            sum += self.numbers[i]
        self.average = sum / len(self.numbers)

    def SolveDispersion(self):
        self._emptyNumbers()
        self.SolveAverage()
        sum = 0
        for i in range(len(self.numbers)):
            sum += math.pow(self.numbers[i]-self.average, 2)
        self.dispersion = sum / (len(self.numbers)-1)

    def exponential(self, size, lambdaValue):
        self.numbers = []
        for i in range(size):
            xi = random.random()
            number = -math.log(xi)/lambdaValue
            self.numbers.append(number)

    def normal(self, size, sigma, alpha):
        self.numbers = []
        for i in range(size):
            mui=0
            for i in range(12):
                mui += random.random()
            mui -= 6
            number = sigma*mui+alpha
            self.numbers.append(number)

    def uniform(self, size, alpha, c):
        self.numbers = []
        z = random.random()
        for i in range(size):
            zNext = alpha*z % c
            self.numbers.append(zNext/c)
            z = zNext
