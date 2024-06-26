persons_board_premise = 4
persons_board_hypothesis = 8

# the hypothesis talks about the number of persons serving in the board of directors of charities, referenced also in the premise
if persons_board_hypothesis <= persons_board_premise:
    # check if the hypothesis value contradicts the estimate of more than 'persons_board_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of persons serving in the board
    # any number of persons greater than 'persons_board_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)