{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0e90ac45-6bf3-4418-8dbc-92974ca67efa",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Возраст Foxy : 8\n",
      "Foxy is a fox\n",
      "\n",
      "Возраст Rex : 15\n",
      "Rex is a dog\n",
      "\n",
      "Возраст Dumbo : 82\n",
      "Dumbo is a elephant\n",
      "\n"
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
    "animals = [\n",
    "    Animal(\"python\", \"Kaa\", 2010),\n",
    "    Animal(\"dog\", \"Balto\", 2005),\n",
    "    Animal(\"elephant\", \"Dumbo\", 2000)\n",
    "]\n",
    "for animal in animals:\n",
    "    print(\"Age\", animal.name, \":\", animal.get_age(2024))\n",
    "    animal.get_info()\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "634b2d42-3646-4161-8f37-003cf340970d",
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
