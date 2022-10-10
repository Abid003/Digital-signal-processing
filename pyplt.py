from cProfile import label
from matplotlib import pyplot as plt


dev_x = [23,24,25,25,26,27,27]
dev_y = [5253,6767,2677,2252,6266,3336,2626]

plt.plot(dev_x,dev_y, label = 'all dev')

py_dev_x = [23,24,25,25,26,27,27]
py_dev_y = [525,676,267,225,626,333,266]

plt.plot(dev_x,py_dev_y, label = 'python')

plt.xlabel('ages')
plt.ylabel('salary ')
plt.title('medium salary by age')

plt.legend(["all dev", "python"])

plt.show()