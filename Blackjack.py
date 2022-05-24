class Card:
    def __init__(self, suit, value, card_value):
        #Determines the suit of the card. Ex: Clubs and Diamonds
        self.suit = suit

        #Represent the Value of the card like A for Ace, and Q for Queen
        self.card_value = card_value

        #Determines the value of each card in the suit
        self.value = value

    def print_cards(cards, hidden):
        s = ""
        for card in cards:
            s = s + "\t ________________"
        if hidden:
            s += "\t ________________"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|                |"
        print(s)

        s = ""
        for card in cards:
            if card.value == "10":
                s = s + "\t|  {}            |".format(card.value)
            else:
                s = s + "\t|  {}              |".format(card.value)
        if hidden:
            s += "\t|                |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|      * *       |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|    *     *     |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|   *       *    |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|   *       *    |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|       {}        |".format(card.suit)
        if hidden:
            s += "\t|          *     |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|         *      |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|        *       |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|                |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|                |"
        print(s)

        s = ""
        for card in cards:
            if card.value == "10":
                s = s + "\t|            {}  |".format(card.value)
            else:
                s = s + "\t|            {}   |".format(card.value)
        if hidden:
            s += "\t|        *       |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|________________|"
        if hidden:
            s += "\t|________________|"
        print(s)

        print()

    