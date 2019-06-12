import unittest

from player import Player


class TestGame(unittest.TestCase):
    def test_get_guess_returns_int(self):
        player = Player("test", 5)
        guess = player.get_guess()
        self.assertIsInstance(guess, int)

    def test_get_guess_same_seed_same_number(self):
        player = Player("test", 5)
        guess1 = player.get_guess(seed=5)
        guess2 = player.get_guess(seed=5)
        self.assertEqual(guess1, guess2)

    def test_get_guess_defaults(self):
        player = Player("test", 5)
        guess = player.get_guess()
        result = guess in range(0,11)
        self.assertEqual(result, True)
    
    
    def test_get_guess_change_to_from_int(self):
        player = Player("test", 5)
        guess = player.get_guess(_from=0, _to=2)
        result = guess in range(0,3)
        self.assertEqual(result, True)


    def test_get_guess_change_to_from_float(self):
        player = Player("test", 5)
        guess = player.get_guess(_from=0, _to=2.3)
        result = guess in range(0,3)
        self.assertEqual(result, True)

    
    def test_get_defense_array_defaults(self):
        player = Player("test", 5)
        defense_array = player.get_defense_array()
        self.assertEqual(5, len(defense_array))
        
    
    def test_get_defense_array_returns_int_array(self):
        player = Player("test", 5)
        defense_array = player.get_defense_array()
        for item in defense_array:
            self.assertIsInstance(item, int)


    def test_get_defense_array_change_to_from_int(self):
        player = Player("test", 5)
        defense_array = player.get_defense_array(_from=0, _to=6)
        for item in defense_array:
            res = item in range(0,7)
            self.assertEqual(res, True)


    def test_get_defense_array_change_to_from_float(self):
        player = Player("test", 5)
        defense_array = player.get_defense_array(_from=0, _to=6.6)
        for item in defense_array:
            res = item in defense_array
            self.assertIsInstance(res, int)


    def test_get_defense_array_zero_defense_array_length(self):
        player = Player("test", 5)
        defense_array = player.get_defense_array()
        self.assertEqual(5, len(defense_array))


if __name__ == '__main__':
    unittest.main()