{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "06f6d36c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "welcome to assignment 1\n"
     ]
    }
   ],
   "source": [
    "print(\"welcome to assignment 1\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cb6037af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NUM1=10\n",
      "NUM2=30\n",
      "Add= 40\n"
     ]
    }
   ],
   "source": [
    "num1=int(input(\"NUM1=\"))\n",
    "num2=int(input(\"NUM2=\"))\n",
    "Add=num1+num2\n",
    "print(\"Add=\",Add)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "374ea78b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the BMI Index=34\n",
      "very over weight\n"
     ]
    }
   ],
   "source": [
    "bmi=float(input(\"Enter the BMI Index=\"))\n",
    "if (bmi<16):\n",
    "    print(\"invalid value\")\n",
    "elif (bmi>=16 and bmi<=18.5):\n",
    "    print(\"Under weight\")\n",
    "elif (bmi<25):\n",
    "    print(\"Normal\")\n",
    "elif (bmi<30):\n",
    "    print(\"over weight\")\n",
    "else:\n",
    "    print(\"very over weight\")\n",
    "    \n",
    "            "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
