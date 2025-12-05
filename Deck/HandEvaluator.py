from Cards.Card import Card, Rank

def evaluate_hand(hand: list[Card]):
    rank_counter = {}
    suit_counter = {}
    same_suit_cards = 0
    highest_rank_count = 0
    is_straight = False
    pairs = 0
    ranks_lst = []
    for card in hand: #Setup of dictionaries
        suit_counter[card.suit.value] = suit_counter.get(card.suit.value, 0) + 1
        rank_counter[card.rank.value] = rank_counter.get(card.rank.value, 0) + 1
    for count in suit_counter.values(): #Counts Same Suit cards in hand
        if count > same_suit_cards:
            same_suit_cards = count
    for count in rank_counter.values(): #Counts Same Rank cards in hand
        if count > highest_rank_count:
            highest_rank_count = count
        if count == 2:
            pairs+=1
    for card_rank in rank_counter.keys():
        ranks_lst.append(card_rank)
    if len(ranks_lst) >= 5: #Ignores if there are less than 5 ranks
        ranks_lst.sort()
        if ([2,3,4,5,14] == ranks_lst or [2,3,4,5,6] == ranks_lst or [3,4,5,6,7] == ranks_lst or [4,5,6,7,8] == ranks_lst
                or [5,6,7,8,9] == ranks_lst or [6,7,8,9,10] == ranks_lst or [7,8,9,10,11] == ranks_lst or [8,9,10,11,12]
                == ranks_lst or [9,10,11,12,13] == ranks_lst or [10,11,12,13,14] == ranks_lst): #Checks for a Straight
            is_straight = True
    if same_suit_cards == 5 and is_straight: #Checks for Straight Flush
        return "Straight Flush"
    elif highest_rank_count == 4:  #Checks for Four of a Kind
        return "Four of a Kind"
    elif  highest_rank_count == 3 and pairs == 1:  #Checks for Full House
        return "Full House"
    elif same_suit_cards == 5: #Checks for Flush
        return "Flush"
    elif is_straight:  #Checks for Straight
        return "Straight"
    elif highest_rank_count == 3:  #Checks for Three of a Kind
        return "Three of a Kind"
    elif pairs == 2:  #Checks for Two Pair
        return "Two Pair"
    elif highest_rank_count == 2:  #Checks for One Pair
        return "One Pair"
    return "High Card" # If none of the above, it's High Card
