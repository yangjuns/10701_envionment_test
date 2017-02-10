import hw1_baseball
import numpy as np


if __name__ == '__main__':
    pre = hw1_baseball.load_data("pre_season.txt")
    mid = hw1_baseball.load_data("mid_season.txt")
    end = hw1_baseball.load_data("end_season.txt")

    # MLE
    MLE = np.divide(mid["hits"], mid["at_bats"])

    #MAP
    total_hits = np.add(pre["hits"], mid["hits"])
    total_ab = np.add(pre["at_bats"], mid["at_bats"])
    MAP = np.divide(total_hits, total_ab)

    hw1_baseball.visualize(pre, mid, end, MLE, MAP, "./")

    # a = np.array([1,2,0.0])
    # b = np.array([1,2,0.0])
    # print np.divide(a,b)