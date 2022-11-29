import unittest
from refactor import Item, Customer


class CartTest(unittest.TestCase):
    def setUp(self):
        self.test_cust = Customer('TestCust')
        self.test_item_one = Item('grape', 2, 20)
        self.test_item_two = Item('banana', 2, 1.25)
        self.test_item_three = Item('apple', 5, .30)
        self.test_item_four = Item('paper towel', 1, 1)
        self.test_cust.add_to_cart(self.test_item_one)
        self.test_cust.add_to_cart(self.test_item_two)
        self.test_cust.add_to_cart(self.test_item_three)
        self.test_cust.add_to_cart(self.test_item_four)

    def test_add_to_cart(self):
        self.test_cust.add_to_cart(self.test_item_one)
        self.assertEqual(self.test_cust.cart['grape'], self.test_item_one)
        self.test_cust.add_to_cart(self.test_item_two)
        self.assertEqual(self.test_cust.cart['banana'], self.test_item_two)
        self.test_cust.add_to_cart(self.test_item_three)
        self.assertEqual(self.test_cust.cart['apple'], self.test_item_three)
        self.test_cust.add_to_cart(self.test_item_four)
        self.assertEqual(
            self.test_cust.cart['paper towel'], self.test_item_four)

    def test_remove_from_cart(self):
        self.test_cust.remove_from_cart('grape')
        self.assertNotIn(self.test_cust.cart, ['grape'])
        self.test_cust.remove_from_cart('banana')
        self.assertNotIn(self.test_cust.cart, ['banana'])
        self.test_cust.remove_from_cart('apple')
        self.assertNotIn(self.test_cust.cart, ['apple'])
        self.test_cust.remove_from_cart('paper towel')
        self.assertNotIn(self.test_cust.cart, ['paper towel'])

    def test_cart_total(self):
        self.assertEqual(self.test_cust.cart_total, 45)


class ItemTest(unittest.TestCase):

    def setUp(self):
        self.test_item_one = Item('grape', 2, 20)
        self.test_item_two = Item('banana', 2, 1.25)
        self.test_item_three = Item('apple', 5, .30)
        self.test_item_four = Item('paper towel', 1, 1)
        self.test_item_five = Item('banana', 1, 1.25)

    def test_subtotal(self):
        self.assertEqual(self.test_item_one.subtotal, 40)
        self.assertEqual(self.test_item_two.subtotal, 2.5)
        self.assertAlmostEqual(self.test_item_three.subtotal, 1.50)
        self.assertEqual(self.test_item_four.subtotal, 1)
        self.assertEqual(self.test_item_five.subtotal, 1.25)

    def test_formatted_name(self):
        self.assertEqual(self.test_item_one.formatted_name, 'grapes')
        self.assertEqual(self.test_item_two.formatted_name, 'bananas')
        self.assertEqual(self.test_item_three.formatted_name, 'apples')
        self.assertEqual(self.test_item_four.formatted_name, 'paper towel')
        self.assertEqual(self.test_item_five.formatted_name, 'banana')


if __name__ == "__main__":
    unittest.main()
