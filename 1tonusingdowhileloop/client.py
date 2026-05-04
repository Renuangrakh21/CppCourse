{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c10afd7f-fadc-4a5d-aa13-ed21b84e206b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factorial of 5 is: 120\n"
     ]
    }
   ],
   "source": [
    "import xmlrpc.client\n",
    "\n",
    "# Connect to server\n",
    "server = xmlrpc.client.ServerProxy(\"http://localhost:8000/\", allow_none=True)\n",
    "\n",
    "try:\n",
    "    n = int(input(\"Enter a number: \"))\n",
    "    result = server.calculate_factorial(n)\n",
    "    print(f\"Factorial of {n} is: {result}\")\n",
    "except Exception as e:\n",
    "    print(\"Error:\", e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e02e8e9-ee46-472b-b1e4-efa7c895bf94",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
