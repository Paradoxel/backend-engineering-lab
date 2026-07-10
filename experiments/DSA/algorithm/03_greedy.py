"""
Greedy Algorithms — Practice
--------------------------------
Greedy means picking the best option available right now,
at each step, without looking back or reconsidering.

This file covers two classic examples: Coin Change and
Activity Selection.
"""
# ---------------------------------------------------------
# Problem 1: Coin Change (minimum number of coins)
# Given a target amount, use the fewest coins possible.
# Greedy: always pick the largest coin that fits -> O(n)
# NOTE: this only works correctly for "nice" coin systems
# like [1, 5, 10, 25]. It can fail for odd coin sets.
# ---------------------------------------------------------

def coin_change_greedy(coins, amout):
    coins = sorted(coins,reverse=True) # largest first
    result=[]
    for coin in coins:
        while amout>= coin: 
            amout-=coin
            result.append(coin)
    return result


# ---------------------------------------------------------
# Problem 2: Activity Selection
# Given start/end times for activities, pick the max number
# of activities that don't overlap.
# Greedy: always pick the activity that finishes earliest -> O(n log n)
# ---------------------------------------------------------
def activity_selection(activities):
    # sort by endtime 
    activities = sorted(activities,key=lambda  x:x[1])
    selected = [activities[0]]
    last_end = activities[0][1]
    for start, end in activities[1:]:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected


if __name__ == "__main__":

    coins = [1, 5, 10, 25]
    amount = 63
    print("Coins available:", coins)
    print(f"Fewest coins for {amount}:", coin_change_greedy(coins, amount))

    activities = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 7)]
    print("\nActivities (start, end):", activities)
    print("Max non-overlapping activities:", activity_selection(activities))