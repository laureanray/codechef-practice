# https://codeforces.com/problemset/problem/1097/A
def solve(card_deck, cards):
    for card in cards:
        card_arr = [char for char in card]
        for c in card_arr:
            if c in [ch for ch in card_deck]:
                return 'YES'
    return 'NO'    

if __name__ == "__main__":
    card_on_deck = input()
    cards_on_hand = []
    cards_on_hand = list(map(str, input().split()))
    print(solve(card_on_deck, cards_on_hand))

