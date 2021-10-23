def cardval(card):
    """
    Function to return int values for comparison
    """
    if card == 'J' or card=='Q' or card=='K':
        return int(10)
    elif card == 'A':
        return int(11)
    else:
        return int(card)

def calc_hand_sum(hand):
    """
    We sort the hand so we get all aces at last. We can now check if every ace would exceed the 21 while iterating over the hand and count it as 1 if so.
    """
    handsum = 0
    hand.sort(key=cardval)
    for item in hand:
        if item == "J" or item == "Q" or item == "K":
            handsum += 10
        elif item == "A":
            if handsum + 11 > 21:
                handsum = handsum + 1
            else:
                handsum = handsum + 11
        else:
            handsum += int(item)
    return handsum

def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """

    sh1 = calc_hand_sum(hand_1)
    sh2 = calc_hand_sum(hand_2)

    if sh1 > 21:
        return False
    if sh2 > 21:
        return True
    if sh1 > sh2:
        return True
    return False
