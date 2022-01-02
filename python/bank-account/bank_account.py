from threading import Lock

def lock(func, *args1, **kwargs1):
    def func_wrapper(self, *args, **kwargs):
        self._lock.acquire()
        result = func(self, *args, **kwargs)
        self._lock.release()
        return result
    return func_wrapper

def is_open(func, *args1, **kwargs1):
    def func_wrapper(self, *args, **kwargs):
        if not self._is_open:
            raise ValueError('This account is closed')
        return func(self, *args, **kwargs)
    return func_wrapper

def is_close(func, *args1, **kwargs1):
    def func_wrapper(self, *args, **kwargs):
        if self._is_open:
            raise ValueError('This account is already open')
        return func(self, *args, **kwargs)
    return func_wrapper


class BankAccount(object):
    def __init__(self):
        self._lock = Lock()
        self._balance = 0
        self._is_open = False

    @is_open
    def get_balance(self):
        return self._balance


    @is_close
    def open(self):
        self._is_open = True

    @lock
    def deposit(self, amount):
        if amount < 0:
            raise ValueError('You cannot deposit negative values')
        self._update_balance(amount)

    @lock
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError('You cannot withdraw negative values')
        self._update_balance(-amount)

    @is_open
    @lock
    def close(self):
        self._is_open = False
        self._balance = 0

    def _update_balance(self, amount):
        newBalance = self.get_balance() + amount

        if newBalance < 0:
            raise ValueError('You cannot withdraw more than deposited')

        self._balance = newBalance
