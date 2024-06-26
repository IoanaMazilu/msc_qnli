persons_board_premise = 4
persons_board_hypothesis = 8

# the hypothesis refers to the number of persons serving on the board of directors of charities in Novel Grove Estates, mentioned also in the premise
if persons_board_hypothesis <= persons_board_premise:
    # check if the number of persons in the hypothesis contradicts the estimate of more than 'persons_board_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of persons
    # any number of persons greater than 'persons_board_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
