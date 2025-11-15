import unittest
from typing import Dict, Tuple


class ShoppingCart:
    def __init__(self) -> None:
        # name -> (unit_price, quantity)
        self._items: Dict[str, Tuple[float, int]] = {}

    def add_item(self, name: str, price: float) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string")
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        if price < 0:
            raise ValueError("Price cannot be negative")

        unit_price = float(price)
        key = name.strip()
        if key in self._items:
            existing_price, qty = self._items[key]
            # Keep original unit price consistent for the item name
            self._items[key] = (existing_price, qty + 1)
        else:
            self._items[key] = (unit_price, 1)

    def remove_item(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string")
        key = name.strip()
        if key not in self._items:
            raise ValueError("Item not found in cart")
        unit_price, qty = self._items[key]
        if qty <= 1:
            del self._items[key]
        else:
            self._items[key] = (unit_price, qty - 1)

    def total_cost(self) -> float:
        return sum(price * qty for price, qty in self._items.values())

    # Convenience for tests and potential UI
    def get_quantity(self, name: str) -> int:
        entry = self._items.get(name.strip())
        return 0 if entry is None else entry[1]

    def get_unit_price(self, name: str) -> float:
        entry = self._items.get(name.strip())
        if entry is None:
            raise ValueError("Item not found in cart")
        return entry[0]


class TestShoppingCart(unittest.TestCase):
    def test_add_single_item(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.5)
        self.assertEqual(cart.get_quantity("Apple"), 1)
        self.assertAlmostEqual(cart.get_unit_price("Apple"), 1.5, places=6)
        self.assertAlmostEqual(cart.total_cost(), 1.5, places=6)

    def test_add_same_item_increments_quantity_and_keeps_unit_price(self):
        cart = ShoppingCart()
        cart.add_item("Banana", 0.99)
        cart.add_item("Banana", 0.50)  # price change ignored; original kept
        self.assertEqual(cart.get_quantity("Banana"), 2)
        self.assertAlmostEqual(cart.get_unit_price("Banana"), 0.99, places=6)
        self.assertAlmostEqual(cart.total_cost(), 0.99 * 2, places=6)

    def test_add_multiple_different_items(self):
        cart = ShoppingCart()
        cart.add_item("Milk", 2.25)
        cart.add_item("Bread", 1.75)
        cart.add_item("Eggs", 3.00)
        self.assertEqual(cart.get_quantity("Milk"), 1)
        self.assertEqual(cart.get_quantity("Bread"), 1)
        self.assertEqual(cart.get_quantity("Eggs"), 1)
        self.assertAlmostEqual(cart.total_cost(), 2.25 + 1.75 + 3.00, places=6)

    def test_remove_item_decrements_quantity(self):
        cart = ShoppingCart()
        cart.add_item("Orange", 1.25)
        cart.add_item("Orange", 1.25)
        self.assertEqual(cart.get_quantity("Orange"), 2)
        cart.remove_item("Orange")
        self.assertEqual(cart.get_quantity("Orange"), 1)
        self.assertAlmostEqual(cart.total_cost(), 1.25, places=6)

    def test_remove_item_completely_when_last_quantity(self):
        cart = ShoppingCart()
        cart.add_item("Yogurt", 0.8)
        self.assertEqual(cart.get_quantity("Yogurt"), 1)
        cart.remove_item("Yogurt")
        self.assertEqual(cart.get_quantity("Yogurt"), 0)
        self.assertAlmostEqual(cart.total_cost(), 0.0, places=6)

    def test_remove_item_not_in_cart_raises(self):
        cart = ShoppingCart()
        with self.assertRaises(ValueError):
            cart.remove_item("NotHere")

    def test_invalid_add_inputs(self):
        cart = ShoppingCart()
        with self.assertRaises(ValueError):
            cart.add_item("", 1.0)
        with self.assertRaises(ValueError):
            cart.add_item("Gum", -0.5)
        with self.assertRaises(ValueError):
            cart.add_item("Gum", "1.0")  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            cart.add_item(None, 1.0)  # type: ignore[arg-type]

    def test_invalid_remove_inputs(self):
        cart = ShoppingCart()
        with self.assertRaises(ValueError):
            cart.remove_item("")
        with self.assertRaises(ValueError):
            cart.remove_item(None)  # type: ignore[arg-type]

    def test_total_cost_precision(self):
        cart = ShoppingCart()
        cart.add_item("A", 0.1)
        cart.add_item("A", 0.1)
        cart.add_item("B", 0.3)
        self.assertAlmostEqual(cart.total_cost(), 0.1 + 0.1 + 0.3, places=7)


if __name__ == "__main__":
    unittest.main()


