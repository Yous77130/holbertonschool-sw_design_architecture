#!/usr/bin/env python3
"""Decorator pattern — beverage topping system."""


class Beverage:
    """Abstract base class for beverages."""

    def cost(self):
        """Return the cost of the beverage."""
        raise NotImplementedError

    def description(self):
        """Return the description of the beverage."""
        raise NotImplementedError


class Coffee(Beverage):
    """A plain coffee beverage."""

    def cost(self):
        """Return the cost of coffee."""
        return 50

    def description(self):
        """Return the description of coffee."""
        return "Coffee"


class MilkDecorator(Beverage):
    """A decorator that adds milk to a beverage."""

    def __init__(self, inner):
        """Initialize with an inner beverage."""
        self._inner = inner

    def cost(self):
        """Return the cost with milk."""
        return self._inner.cost() + 10

    def description(self):
        """Return the description with milk."""
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """A decorator that adds sugar to a beverage."""

    def __init__(self, inner):
        """Initialize with an inner beverage."""
        self._inner = inner

    def cost(self):
        """Return the cost with sugar."""
        return self._inner.cost() + 5

    def description(self):
        """Return the description with sugar."""
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """A decorator that adds caramel to a beverage."""

    def __init__(self, inner):
        """Initialize with an inner beverage."""
        self._inner = inner

    def cost(self):
        """Return the cost with caramel."""
        return self._inner.cost() + 15

    def description(self):
        """Return the description with caramel."""
        return self._inner.description() + " + caramel"


def main():
    """Main function."""
    b1 = MilkDecorator(Coffee())
    print(b1.description(), b1.cost())

    b2 = MilkDecorator(SugarDecorator(Coffee()))
    print(b2.description(), b2.cost())

    b3 = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(b3.description(), b3.cost())


if __name__ == "__main__":
    main()
