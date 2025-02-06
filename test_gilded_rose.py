# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)
    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEqual(["Sulfuras"], all_items)

    #The first test focusing on logical errors
    def test_sellby_passed_quality_decreases_twice(self):
        items = [Item("Conjured", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        conjured_item = items[0]
        self.assertEqual(16,conjured_item.quality)
        self.assertEqual(-1, conjured_item.sell_in)
        self.assertEqual("Conjured", conjured_item.name)

    #The second test focusing on logical errors
    def test_conjured_degrade_twice(self):
        items = [Item("Conjured", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        conjured_item = items[0]
        self.assertEqual(78, conjured_item.quality)
        self.assertEqual(4, conjured_item.sell_in)
        self.assertEqual("Conjured", conjured_item.name)

    #The third test focusing on logical errors
    def test_backstage_quality_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        backstage_passes_item = items[0]
        self.assertEqual(0,backstage_passes_item.quality)
        self.assertEqual(-1, backstage_passes_item.sell_in)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", backstage_passes_item.name)

    def test_sulfuras_should_not_decrease_sellin(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(79, sulfuras_item.quality)
        self.assertEqual(5, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # test that checks for syntax errors
    def test_item_get_name(self):
        sulfuras_item = Item("Sulfuras", 5, 80)
        item_name= sulfuras_item.get_name()
        self.assertEqual("Sulfuras", item_name)

if __name__ == '__main__':
    unittest.main()
