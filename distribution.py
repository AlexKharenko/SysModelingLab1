import math
from scipy.stats import norm
from generator import NumberGenerator


class Distribution:
    def __init__(self, generator: NumberGenerator, numberOfIntervals=20):
        self.generator = generator
        self.numberOfIntervals = numberOfIntervals

    def FxExponential(self, x):
        self.generator.SolveAverage()
        self.generator.SolveDispersion()
        average = self.generator.average
        dispersion = math.sqrt(self.generator.dispersion)
        lambdaValue = (1/average+1/dispersion)/2
        result = 1-math.pow(math.e, -x*lambdaValue)
        return result

    def FxUniform(self, x):
        return x

    def ArrayMin(self, arr):
        min = arr[0]
        for i in range(len(arr)):
            if arr[i] < min:
                min = arr[i]
        return min

    def ArrayMax(self, arr):
        max = arr[0]
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]
        return max

    def sizeOfInterval(self, min, max):
        intervalSize = (max-min)/self.numberOfIntervals
        return intervalSize

    def facticalHitting(self, current, previous):
        counter = 0
        for i in range(len(self.generator.numbers)):
            if self.generator.numbers[i] > current:
                break
            if self.generator.numbers[i] >= previous:
                counter += 1
        return counter

    def theoreticalHitting(self, FxMethod, current, previous):
        return FxMethod(current) - FxMethod(previous)

    def XiSquare(self, FxMethod):
        theory , fact, intervalCount, Xi = 0, 0, 0, 0
        minValue = self.ArrayMin(self.generator.numbers)
        maxValue = self.ArrayMax(self.generator.numbers)
        intervalSize = self.sizeOfInterval(minValue, maxValue)
        merge = False
        self.generator.numbers.sort()
        previous = minValue
        current = minValue+intervalSize
        for i in range(self.numberOfIntervals):
            fact = self.facticalHitting(current, previous)
            theory = int(self.theoreticalHitting(
                FxMethod, current, previous) * len(self.generator.numbers))
            if theory >= 5 and fact >= 5:
                if merge:
                    previous = current
                    merge = False
                else:
                    previous += intervalSize
                current += intervalSize
            else:
                current += intervalSize
                merge = True
                continue
            intervalCount += 1
            Xi += math.pow(fact - theory, 2) / theory
        return Xi


    def theoreticalHittingNormal(self, current, previous, alpha, sigma):
        return norm.cdf(current, loc=alpha, scale=sigma) - norm.cdf(previous, loc=alpha, scale=sigma)

    def XiSquareNormal(self, alpha, sigma):
        theory , fact, intervalCount, Xi = 0, 0, 0, 0
        minValue = self.ArrayMin(self.generator.numbers)
        maxValue = self.ArrayMax(self.generator.numbers)
        intervalSize = self.sizeOfInterval(minValue, maxValue)
        merge = False
        self.generator.numbers.sort()
        previous = minValue
        current = minValue+intervalSize
        for i in range(self.numberOfIntervals):
            fact = self.facticalHitting(current, previous)
            theory = int(self.theoreticalHittingNormal(
                current, previous, alpha, sigma) * len(self.generator.numbers))
            if theory >= 5 and fact >= 5:
                if merge:
                    previous = current
                    merge = False
                else:
                    previous += intervalSize
                current += intervalSize
            else:
                current += intervalSize
                merge = True
                continue
            intervalCount += 1
            Xi += math.pow(fact - theory, 2) / theory
        return Xi