import numpy as np
import pandas as pd



def readFile(file='a_example.in'):
    names = ['xStart','yStart','xFinish','yFinish','earliestStart','latestFinish']
    df = pd.read_csv(file,skiprows=[0],header=None,names=names,delimiter=' ')
    return df


if __name__ == "__main__":
    print('Functions imported   ')