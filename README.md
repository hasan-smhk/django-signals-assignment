# django-signals-assignment

# Django Signals Assignment

 Questions Covered

Question 1
Are Django signals synchronous or asynchronous by default?

Answer:
Django signals execute synchronously by default.

URL:
http://127.0.0.1:8000/sync/


Question 2
Do Django signals run in the same thread?

Answer: Yes.

The thread IDs printed in the view and the signal are identical.

Question 3
Do Django signals run in the same database transaction?

Answer: Yes.

The transaction rollback example demonstrates that the signal runs within the same transaction.

 Installation

bash
git clone <repository-url>
cd django_signals_assignment

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

Visit:


http://127.0.0.1:8000/sync/

and

http://127.0.0.1:8000/transaction/


**
Topic: Custom Classes in Python**

class Rectangle:

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}


# Example usage
rectangle = Rectangle(10, 5)

for item in rectangle:
    print(item)
    
Output
{'length': 10}
{'width': 5}
