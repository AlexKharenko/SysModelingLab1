import random
from distribution import Distribution

from generator import NumberGenerator
from chart import Chart


def main():
    arraySize = 10000
    shouldClose = False
    numberGenerator = NumberGenerator()
    distribution = Distribution(numberGenerator)
    while not shouldClose:
        print('Choose option:\n1-Exponential\n2-Normal\n3-Uniform\n0-Exit\n')
        inputValue = int(input("Enter option number: "))
        if inputValue == 1:
            lambdaValue = random.randint(1,50)
            print('params: ', lambdaValue)
            numberGenerator.exponential(arraySize, lambdaValue)
            numberGenerator.SolveAverage()
            print('Average: ', numberGenerator.average)
            numberGenerator.SolveDispersion()
            print('Dispersion: ', numberGenerator.dispersion)
            XiSquare = distribution.XiSquare(distribution.FxExponential)
            print('Xi^2: ', XiSquare)
            chart = Chart(numberGenerator.numbers, 'Exponential')
            chart.show()
        if inputValue == 2:
            sigma = random.randint(1,10)
            alpha = random.randint(1, 10)
            print('sigma: ', sigma)
            print('alpha: ', alpha)
            numberGenerator.normal(arraySize, sigma, alpha)
            numberGenerator.SolveAverage()
            print('Average: ', numberGenerator.average)
            numberGenerator.SolveDispersion()
            print('Dispersion: ', numberGenerator.dispersion)
            XiSquare = distribution.XiSquareNormal(alpha, sigma)
            print('Xi^2: ', XiSquare)
            chart = Chart(numberGenerator.numbers, 'Normal')
            chart.show()
        if inputValue == 3:
            sigma = random.randint(2,10)
            c = random.randint(2, 10)
            firstPow = random.randint(2, 30)
            secondPow = random.randint(2, 30)
            print('sigma^'+str(firstPow)+': ', sigma)
            print('c^'+str(secondPow)+': ', c)
            numberGenerator.uniform(arraySize, pow(sigma, firstPow), pow(c, secondPow))
            numberGenerator.SolveAverage()
            print('Average: ', numberGenerator.average)
            numberGenerator.SolveDispersion()
            print('Dispersion: ', numberGenerator.dispersion)
            XiSquare = distribution.XiSquare(distribution.FxUniform)
            print('Xi^2: ', XiSquare)
            chart = Chart(numberGenerator.numbers, 'Uniform')
            chart.show()
        if(inputValue == 0):
            shouldClose=True

            

main()