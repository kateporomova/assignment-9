{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "93bc4160-c982-4f15-b812-69da60883560",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Age Kaa : 14\n",
      "Kaa is a python\n",
      "\n",
      "Age Balto : 19\n",
      "Balto is a dog\n",
      "\n",
      "Age Dumbo : 24\n",
      "Dumbo is a elephant\n",
      "\n",
      "The oldest animal Dumbo elephant 24\n"
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
    "    def find_oldest_animal(animals):\n",
    "        oldest_animal = animals[0]\n",
    "        for animal in animals:\n",
    "            if animal.get_age(2024) > oldest_animal.get_age(2024):\n",
    "                oldest_animal = animal\n",
    "        return oldest_animal\n",
    "animals = [\n",
    "    Animal(\"python\", \"Kaa\", 2010),\n",
    "    Animal(\"dog\", \"Balto\", 2005),\n",
    "    Animal(\"elephant\", \"Dumbo\", 2000)\n",
    "]\n",
    "for animal in animals:\n",
    "    print(\"Age\", animal.name, \":\", animal.get_age(2024))\n",
    "    animal.get_info()\n",
    "    print()\n",
    "oldest_animal = Animal.find_oldest_animal(animals)\n",
    "print(\"The oldest animal\", oldest_animal.name, oldest_animal.genus, oldest_animal.get_age(2024))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0f08d4f-750e-4369-9b26-188c6c4f8a44",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "223a76f0-5a1c-4311-954f-1effc55faf68",
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
