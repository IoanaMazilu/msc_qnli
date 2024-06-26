persons_board_premise = 8
persons_board_hypothesis = 8

# the hypothesis refers to the number of persons serving on the board of directors in each charity, mentioned in the premise
if persons_board_hypothesis <= persons_board_premise:
    # check if the hypothesis value contradicts the number of persons in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
