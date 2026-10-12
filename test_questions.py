import re
import unittest
from unittest.mock import patch

import questions


class SurfaceAreaT1Tests(unittest.TestCase):
    def test_two_by_two_tiles_on_10_by_4_rectangle(self):
        with patch("questions.random.randint", side_effect=[5, 2]):
            q, ans = questions.surface_area_t1()

        match = re.search(r"(\d+) in wide by (\d+) in long", q)
        width, length = map(int, match.groups())
        self.assertEqual((width, length), (10, 4))
        self.assertEqual(ans, 10)
        self.assertIsInstance(ans, int)
        self.assertIn("2 in-by-2 in", q)


if __name__ == "__main__":
    unittest.main()
