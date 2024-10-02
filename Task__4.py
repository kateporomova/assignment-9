{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2c52d059-348d-4ce2-bf1f-c36a72745e20",
   "metadata": {
    "tags": []
   },
   "outputs": [],
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
    "    def save_to_file(self, filename):\n",
    "        with open(filename, \"w\") as file:\n",
    "            file.write(f\"{self.name}\\t{self.genus}\\n\")\n",
    "animals = [\n",
    "    Animal(\"python\", \"Kaa\", 2010),\n",
    "    Animal(\"dog\", \"Balto\", 2005),\n",
    "    Animal(\"elephant\", \"Dumbo\", 2000)\n",
    "]\n",
    "for animal in animals:\n",
    "    animal.save_to_file(\"animals.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bcce479-380d-4976-9895-9405a3806277",
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
