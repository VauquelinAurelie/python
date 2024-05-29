def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return f"{year} est une année bissextile."
    else:
        return f"{year} n'est pas une année bissextile."

    def test_leap_year():
        assert leap_year(2015)


