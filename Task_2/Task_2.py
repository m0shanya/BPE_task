def find_fake_basket(N, w, d, P):
    """Weight calculation using arithmetic progression"""
    total_weight = (1 + N) * N * w / 2 - P  # common weight without fake coins
    expected_weight = 0

    for i in range(1, N + 1):
        expected_weight += i * w  # expected weight in this basket
        if abs(total_weight - expected_weight) == d:
            print("Fake basket have number", i)
            break


find_fake_basket(5, 10, 5, 85)
