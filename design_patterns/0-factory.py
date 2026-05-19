#!/usr/bin/env python3
"""Factory pattern — vehicle registry."""


class Bus:
    """A bus vehicle."""

    def mode(self):
        """Return the mode of transport."""
        return "road"


class Train:
    """A train vehicle."""

    def mode(self):
        """Return the mode of transport."""
        return "rails"


class Bike:
    """A bike vehicle."""

    def mode(self):
        """Return the mode of transport."""
        return "lane"


class Scooter:
    """A scooter vehicle."""

    def mode(self):
        """Return the mode of transport."""
        return "scooter_lane"


class VehicleFactory:
    """A factory that creates vehicles from a registry."""

    def __init__(self):
        """Initialize the factory with default vehicles."""
        self._registry = {}
        self.register_kind("bus", Bus)
        self.register_kind("train", Train)
        self.register_kind("bike", Bike)

    def register_kind(self, name, cls):
        """Register a new vehicle type."""
        self._registry[name] = cls

    def create(self, kind):
        """Create a vehicle by kind."""
        if kind not in self._registry:
            raise ValueError("Unknown vehicle: {}".format(kind))
        return self._registry[kind]()


def main():
    """Main function."""
    factory = VehicleFactory()
    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
