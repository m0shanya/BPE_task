def find_fake_basket(N, w, d, P):
    a = (N * (N - 1)) // 2
    expected_total_weight = a * w
    actual_total_weight = P + (w - d) * a
    fake_basket = abs((expected_total_weight - actual_total_weight)) // (w - d)
    return fake_basket  # индексная коррекция


# Пример использования
N = 3
w = 10
d = 3
P = 27
fake_basket = find_fake_basket(N, w, d, P)
print(fake_basket)
