{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1cf26e3b-946a-4ef6-b7f5-1c4b23eb8511",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Server started on http://localhost:8000/\n"
     ]
    }
   ],
   "source": [
    "from xmlrpc.server import SimpleXMLRPCServer\n",
    "import threading\n",
    "\n",
    "# Factorial function with validation\n",
    "def factorial(n):\n",
    "    if not isinstance(n, int):\n",
    "        return \"Error: Input must be integer\"\n",
    "    if n < 0:\n",
    "        return \"Error: Negative number not allowed\"\n",
    "    \n",
    "    result = 1\n",
    "    for i in range(2, n + 1):\n",
    "        result *= i\n",
    "    return result\n",
    "\n",
    "# Function to run server\n",
    "def start_server():\n",
    "    server = SimpleXMLRPCServer((\"localhost\", 8000), logRequests=True, allow_none=True)\n",
    "    server.register_function(factorial, \"calculate_factorial\")\n",
    "    print(\"Server started on http://localhost:8000/\")\n",
    "    server.serve_forever()\n",
    "\n",
    "# Run server in background thread (IMPORTANT for Jupyter)\n",
    "server_thread = threading.Thread(target=start_server)\n",
    "server_thread.daemon = True\n",
    "server_thread.start()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57f254d7-a283-44b9-aa02-d008890026b1",
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
