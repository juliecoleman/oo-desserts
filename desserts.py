"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


    def __init__(self, name, flavor, price):

      self.name = name
      self.flavor = flavor
      self.price = price
      self.qty = 0
      self.cache[name] = self

    def add_stock(self, amount):

      self.qty = self.qty + amount

    def sell(self, amount):

      if self.qty == 0:
        print('Sorry, these cupcakes are sold out')
        return

      elif amount > self.qty:
        self.qty = 0
        return

      else:
        self.qty = self.qty - amount

    
    @staticmethod
    def scale_recipe(ingredients, amount):

      new_ingredients = []

      for ingredient in ingredients:
          new_ingredient = (ingredient[0], ingredient[1] * amount)
          new_ingredients.append(new_ingredient)

      return new_ingredients

#       return [(ingredient, qty * amount)
#               for ingredient, qty in ingredients]

    @classmethod
    def get(cls, name):

      if name in cls.cache:
        return cls.cache[name]

      else:
        return print("Sorry, that cupcake doesn't exist")


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
