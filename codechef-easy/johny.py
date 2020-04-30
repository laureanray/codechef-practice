# https://www.codechef.com/problems/JOHNY
def binary_search(arr, low, high, x):
    # base case
    if high >= low:
        mid = low + (high - low) // 2
        # if el is present in the middle
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


if __name__ == "__main__":
    res = []      
    for x in range(int(input())):
        num_songs = int(input())
        playlist = list(map(int, input().strip().split(' ')))
        k = int(input())
        to_find = playlist[k-1]
        playlist.sort()
        print(binary_search(playlist, 0, len(playlist) - 1, to_find) + 1)
