import unittest
import sys
import os
import json

# Add the parent directory to the path so we can import manage_cards
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

import manage_cards

class TestCards(unittest.TestCase):

    def setUp(self):
        self.v_cards_file = os.path.join(base_dir, "cards", "vulnerability_cards.json")
        self.i_cards_file = os.path.join(base_dir, "cards", "infrastructure_cards.json")

    def test_vulnerability_cards_structure(self):
        """Test that vulnerability cards have the correct structure."""
        cards = manage_cards.load_cards(self.v_cards_file)
        self.assertTrue(len(cards) > 0, "No vulnerability cards loaded")
        for card in cards:
            self.assertIn('id', card)
            self.assertIn('name', card)
            self.assertIn('description', card)
            self.assertIn('severity', card)
            self.assertIn('cost', card)
            self.assertIn('effect', card)

    def test_infrastructure_cards_structure(self):
        """Test that infrastructure cards have the correct structure."""
        cards = manage_cards.load_cards(self.i_cards_file)
        self.assertTrue(len(cards) > 0, "No infrastructure cards loaded")
        for card in cards:
            self.assertIn('id', card)
            self.assertIn('name', card)
            self.assertIn('description', card)
            self.assertIn('defense', card)
            self.assertIn('cost', card)
            self.assertIn('effect', card)

    def test_find_card(self):
        """Test finding a card by ID."""
        cards = manage_cards.load_cards(self.v_cards_file)
        card = manage_cards.find_card(cards, "v-001")
        self.assertIsNotNone(card)
        self.assertEqual(card['id'], "v-001")
        self.assertEqual(card['name'], "SQL Injection")

    def test_find_card_not_found(self):
        """Test finding a non-existent card."""
        cards = manage_cards.load_cards(self.v_cards_file)
        card = manage_cards.find_card(cards, "non-existent-id")
        self.assertIsNone(card)

if __name__ == '__main__':
    unittest.main()
