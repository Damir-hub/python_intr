import pytest

from calculator import calculate_sum


# def test_calculate_sum_positive_numbers():
#     # assert - утверждение
#     assert calculate_sum(10, 10) == 20
#
#
# def test_calculate_sum_one_negative_numbers():
#     # assert - утверждение
#     assert calculate_sum(11, -5 ) == 6
#
#
# def test_calculate_sum_one_zero_numbers():
#     # assert - утверждение
#     assert calculate_sum(7, 0 ) == 7


# parametrize - позволяет один раз написать тестувую функцию и многократно ее вызывать с разным набором параметров
@pytest.mark.parametrize("number1, number2, expected_result", [
    (10, 10, 20),
    (20, -30, -10),
    (-50, -40, -90),
    (0, 0, 0),
])
def test_calculate_sum(number1, number2, expected_result):
    assert calculate_sum(number1, number2) == expected_result


# xfail- маркировка падающего теста
@pytest.mark.xfail(reason="Известная проблема с отрицательными числами")
def test_calculate_sum_two_negative_numbers():
    # assert - утверждение
    assert calculate_sum(-8, -9 ) >= 0


# skip - маркировка недописанного автотеста, который не стоит запускать (пропустить)
@pytest.mark.skip(reason="Автотест не готов")
def test_calculate_sum_two_zero_numbers():
    # assert - утверждение
    assert calculate_sum(0, 0 ) == 0