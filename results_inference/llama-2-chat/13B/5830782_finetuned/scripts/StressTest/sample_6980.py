persons_board_premise = 8
persons_board_hypothesis = 8

# the hypothesis refers to the number of persons serving in the board of directors of charities in the premise
if persons_board_hypothesis >= persons_board_premise:
    # check if the hypothesis value contradicts the exact number of 'persons_board_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
