{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {},
   "outputs": [],
   "source": [
    "def maxTuples(a, n, m):\n",
    "    for k in range (0, n):\n",
    "        maxx = 0\n",
    "        maxi = 0\n",
    "        maxj = 0 \n",
    "        for i in range (0, n):\n",
    "            for j in range (0, m): \n",
    "                if a[i][j] > maxx:\n",
    "                    maxx = a[i][j]\n",
    "                    maxi = i\n",
    "                    maxj = j\n",
    "        for i in range (0, m):\n",
    "            a[maxi][i] = -1\n",
    "        for j in range (0, n):\n",
    "            a[j][maxj] = -1  \n",
    "        print (maxx, maxi, maxj)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'matrix' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-159-adbe140d66f1>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mmaxTuples\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmatrix\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mn\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mm\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'matrix' is not defined"
     ]
    }
   ],
   "source": [
    "maxTuples(matrix, n, m)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "def returnMatrix():\n",
    "    n, m = 3, 4;\n",
    "    a = [[0 for x in range(m)] for y in range(n)] \n",
    "\n",
    "    a[0][0] = 1\n",
    "    a[0][1] = 5\n",
    "    a[0][2] = 7\n",
    "    a[0][3] = 3\n",
    "    a[1][0] = 2\n",
    "    a[1][1] = 4\n",
    "    a[1][2] = 3\n",
    "    a[1][3] = 6\n",
    "    a[2][0] = 6\n",
    "    a[2][1] = 8\n",
    "    a[2][2] = 15\n",
    "    a[2][3] = 9\n",
    "\n",
    "    return a\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
