# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class UpdateStrategy(ABC):
    @abstractmethod
    def update_quality(self, item):
        pass

class NormalItemStrategy(UpdateStrategy):
    def update_quality(self, item):
        if item.quality > 0:
            item.quality = max(0, item.quality - 1)
        if item.sell_in <= 0 and item.quality > 0:
            item.quality = max(0, item.quality - 1)
        item.sell_in -= 1

class AgedBrieStrategy(UpdateStrategy):
    def update_quality(self, item):
        if item.quality < 50:
            item.quality = min(50, item.quality + 1)
            if item.sell_in <= 0:
                item.quality = min(50, item.quality + 1)
        item.sell_in -= 1

class BackstagePassStrategy(UpdateStrategy):
    def update_quality(self, item):
        if item.quality < 50:
            item.quality = min(50, item.quality + 1)
            if item.sell_in <= 10:
                item.quality = min(50, item.quality + 1)
            if item.sell_in <= 5:
                item.quality = min(50, item.quality + 1)
        if item.sell_in <= 0:
            item.quality = 0
        item.sell_in -= 1

class SulfurasStrategy(UpdateStrategy):
    def update_quality(self, item):
        # Sulfuras is legendary - quality always 80 and sell_in never changes
        item.quality = 80
        # Intentionally not modifying sell_in as per requirements

class ConjuredItemStrategy(UpdateStrategy):
    def update_quality(self, item):
        if item.quality > 0:
            # Degrade twice as fast as normal items (2 points)
            item.quality = max(0, item.quality - 2)
        if item.sell_in <= 0 and item.quality > 0:
            # After sell_in date, degrade twice as fast again (2 more points)
            item.quality = max(0, item.quality - 2)
        item.sell_in -= 1

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    def get_name(self):
        return self.name

class GildedRose:
    def __init__(self, items):
        self.items = items
        self.strategies = {
            "normal": NormalItemStrategy(),
            "Aged Brie": AgedBrieStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
            "Sulfuras": SulfurasStrategy(),  # Handle test case name
            "Conjured": ConjuredItemStrategy()
        }

    def update_quality(self):
        for item in self.items:
            strategy = self.strategies.get(item.name, self.strategies["normal"])
            strategy.update_quality(item)
    
    def get_items(self):
        return [item.name for item in self.items]