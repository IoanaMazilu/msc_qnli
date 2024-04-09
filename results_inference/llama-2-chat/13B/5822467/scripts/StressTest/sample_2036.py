women_board_premise = 4
men_board_premise = 0
women_board_hypothesis = 7
men_board_hypothesis = 0

# the hypothesis refers to the difference between the number of women and men on the board
if women_board_hypothesis - men_board_hypothesis == women_board_premise - men_board_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif women_board_hypothesis - men_board_hypothesis!= women_board_premise - men_board_premise:
    # check if the difference between the number of women and men in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference between the number of women and men
    # any difference greater than 'women_board_premise - men_board_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
