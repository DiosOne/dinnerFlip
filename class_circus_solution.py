"""
This module contains functions for calculating ticket prices for performers.
"""
def calculate_ticket_price_for_performer(regular_ticket_price, performer_type):
    """
    Calculate the ticket price for a performer based on their type.

    Args:
        regular_ticket_price (float): The regular ticket price.
        performer_type (str): The type of performer.

    Returns:
        float: The calculated ticket price.

    Notes:
        The ticket price is calculated based on the performer type.
        The discount rates are as follows:
        - Juggler: 50%
        - Fire Twirler: 25%
        - Magician: 80%
        - Escape Artist: 100% (free)
        - Others: 20%
    """
    if performer_type == "Juggler":
        return regular_ticket_price * 0.5
    elif performer_type == "Fire Twirler":
        return regular_ticket_price * 0.75
    elif performer_type == "Magician":
        return regular_ticket_price * 0.2
    elif performer_type == "Escape Artist":
        return 0
    else:
        return regular_ticket_price * 0.8
