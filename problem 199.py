# PAYMENT SYSTEM USING ABSTRACT METHOD

from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(Payment):
    def pay(self,amount):
        print("paid",amount,"using UPI")

class Card(Payment):
    def pay(self,amount):
        print("paid",amount,"using Card")

u = UPI()
c = Card()

u.pay(288)
c.pay(889)