# Write your code below:
import surfshop
import unittest 

class TestSurfShop(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.cart = surfshop.ShoppingCart()
    

    # ORIGINAL WITH ONE INPUT HARD-CODED IN... 
    # def test_add_surfboards(self):
    #     self.assertEqual(self.cart.add_surfboards(1), 
    #                     ('Successfully added 1 surfboard to cart!'), 'This should return 1 surfboard')

    def test_add_surfboards(self):
        for amount in [2, 3, 4]:
            with self.subTest(amount):
                message = self.cart.add_surfboards(amount)
                self.assertEqual(message, f'Successfully added {amount} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()

    ### assertRaises:  ###
    # The assertRaises() method takes an exception type as its 
    # first argument, a function reference as its second, and an arbitrary 
    # number of arguments as the rest.
        # self.assertRaises(specificException, function, functionArguments...)
    def test_add_too_many_surfboards(self):
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

    
    ### EXPECTED FAILURES ###
    @unittest.expectedFailure
    def test_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount) 

    

unittest.main()



    

    




unittest.main()