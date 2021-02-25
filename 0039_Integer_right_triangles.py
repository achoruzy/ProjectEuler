# PROBLEM 39

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

# ----------- PSEUDOCODE -------------
# make loop, get next p up to 1000
# find number of side-lenght solutions for p:
# condition: a^2 + b^2 = c^2 and a+b+c=p; a,b,c,p are integers
# notes: c > a, b
# return p having the most solutions


# -------------- CODE ----------------

def triangle_side_gen(perimeter: int) -> list:
    """ Yields next triple of sides for a triangle with given perimeter """
    for c in range(int(perimeter/2), 2, -1):
        for b in range(perimeter-c-1, int((perimeter-c-1)/2), -1):
            a = perimeter-c-b
            if c < 1 or b < 1 or a < 1:
                continue
            if b >= c:
                continue
            yield [c, b, a]


def is_right_angle(sides: list) -> bool:
    """ Checks if a^2+b^2 == c^2 for the list of sides """
    c = sides[0]
    b = sides[1]
    a = sides[2]

    if (a*a) + (b*b) == (c*c):
        return True
    else:
        return False

# -------------- TESTS ---------------


def test_triangle_side_gen():
    # given
    perimeter = 10
    # when
    gen = triangle_side_gen(10)
    first = next(gen)
    second = next(gen)
    third = next(gen)
    # then
    assert type(first) == list
    assert first != second
    assert third == [4, 3, 3]


def test_is_right_angle():
    # given
    check_list = [52, 48, 20]
    # when
    result = is_right_angle(check_list)
    # then
    assert type(result) == bool
    assert result == True
    assert is_right_angle([10, 3, 3]) == False


# --------------- RUN ---------------
if __name__ == '__main__':
    perimeter = 9
    most_solutions = [0, 0]
    while perimeter <= 1000:
        perimeter += 1
        help_counter = 0
        for i in triangle_side_gen(perimeter):
            if is_right_angle(i):
                help_counter += 1
        if help_counter > most_solutions[0]:
            most_solutions[0] = help_counter
            most_solutions[1] = perimeter

    print(most_solutions)


# ------------ RESULT -------------
# [8, 840]
