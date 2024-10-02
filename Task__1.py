{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "79f237f8-2a7f-400b-83db-1a8ef5cebbd5",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Age of Dumbo: 24\n",
      "Kaa is a python\n",
      "Information of Kaa: None\n"
     ]
    }
   ],
   "source": [
    "class Animal:\n",
    "    def __init__(self, genus, name, year_of_birth):\n",
    "        self.genus = genus\n",
    "        self.name = name\n",
    "        self.year_of_birth = year_of_birth\n",
    "    def get_age(self, current_year):\n",
    "        return current_year - self.year_of_birth\n",
    "    def get_info(self):\n",
    "        print(f\"{self.name} is a {self.genus}\")\n",
    "Animal_1 = Animal(\"elephant\", \"Dumbo\", 2000)\n",
    "Animal_2 = Animal(\"python\", \"Kaa\", 2010)\n",
    "print(\"Age of Dumbo:\", Animal_1.get_age(2024))\n",
    "print(\"Information of Kaa:\", Animal_2.get_info())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f406bcc-7491-445b-a289-ec4ec2fae7a2",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
