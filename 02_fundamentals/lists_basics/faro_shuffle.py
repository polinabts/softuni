cards = input().split()
shuffles_count = int(input())

shuffled_cards = cards
current_shuffle = []

for shuffle in range (shuffles_count):
    current_shuffle = []

    middle = int(len(cards) / 2)

    first_half = shuffled_cards[:middle]

    for i in range(middle):
        first_card = first_half[i]
        second_card = shuffled_cards[i + middle]

        current_shuffle.append(first_card)
        current_shuffle.append(second_card)
    shuffled_cards = current_shuffle


print(shuffled_cards)