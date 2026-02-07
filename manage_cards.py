import json
import os

def load_cards(filename):
    """Loads cards from a JSON file."""
    try:
        with open(filename, 'r') as f:
            cards = json.load(f)
        return cards
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filename}'.")
        return []

def list_cards(cards, card_type="Card"):
    """Prints the list of cards."""
    print(f"\n--- {card_type}s ---")
    if not cards:
        print("No cards found.")
        return

    for card in cards:
        print(f"ID: {card.get('id')}")
        print(f"Name: {card.get('name')}")
        print(f"Description: {card.get('description')}")
        if 'severity' in card:
            print(f"Severity: {card.get('severity')}")
        if 'defense' in card:
            print(f"Defense: {card.get('defense')}")
        print(f"Cost: {card.get('cost')}")
        print(f"Effect: {card.get('effect')}")
        print("-" * 20)

def find_card(cards, card_id):
    """Finds a card by ID."""
    for card in cards:
        if card.get('id') == card_id:
            return card
    return None

if __name__ == "__main__":
    v_cards_file = "cards/vulnerability_cards.json"
    i_cards_file = "cards/infrastructure_cards.json"

    print("Loading Vulnerability Cards...")
    v_cards = load_cards(v_cards_file)
    list_cards(v_cards, "Vulnerability Card")

    print("\nLoading Infrastructure Cards...")
    i_cards = load_cards(i_cards_file)
    list_cards(i_cards, "Infrastructure Card")
