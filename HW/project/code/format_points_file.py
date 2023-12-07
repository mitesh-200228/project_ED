import sys

# third party library
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        data = np.loadtxt(filename)
        assert(data.shape[1] == 2)
        np.savetxt(filename, data, delimiter='\t')
