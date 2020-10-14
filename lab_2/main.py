from scipy.stats import uniform, poisson
from matplotlib import pyplot as plt
import numpy as np


def uniform_distribution(a, b):
	indent = (b - a) // 2
	x = np.linspace(a - indent, b + indent, 100)

	dist = uniform(loc=a, scale=abs(a - b))

	figure, (ax_1, ax_2) = plt.subplots(1, 2, figsize=(16, 9))
	figure.suptitle('Равномерное распределение')

	ax_1.plot(x, dist.cdf(x), color='darkorange', label=f'F({a}, {b})')
	ax_1.set_title('Функция распределения')
	ax_1.legend(loc='upper left')

	ax_2.plot(x, dist.pdf(x), color='darkturquoise', label=f'F({a}, {b})')
	ax_2.set_title('Функция плотности распределения')
	ax_2.legend(loc='upper left')

	plt.show()


def poisson_distribution(mu):
	x = np.arange(-1, 20)

	dist = poisson(mu)

	figure, (ax_1, ax_2) = plt.subplots(1, 2, figsize=(16, 9))
	figure.suptitle('Пуассоновское распределение')

	ax_1.plot(x, dist.cdf(x), color='darkorange', label=f'F({mu})')
	ax_1.set_title('Функция распределения')
	ax_1.legend(loc='upper left')

	ax_2.plot(x, dist.pmf(x), color='darkturquoise', label=f'f({mu})')
	ax_2.set_title('Функция плотности распределения')
	ax_2.legend(loc='upper left')

	plt.show()


def main():
	uniform_distribution(-1, 1)
	poisson_distribution(10)


if __name__ == '__main__':
	main()
