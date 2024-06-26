persons_board_premise = 8
persons_board_hypothesis = 8

# the hypothesis refers to the number of persons serving in the board of directors of charities
if persons_board_hypothesis >= persons_board_premise:
    # check if the hypothesis value contradicts the exact number of persons in the board according to the premise
    label = "contradiction"
else:
    # the premise gives an exact number of persons in the board
    # any number of persons less than 'persons_board_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
