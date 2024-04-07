# Premise: Each of three charities in Novel Grove Estates has 8 persons serving on its board of directors.
# Hypothesis: Each of three charities in Novel Grove Estates has more than 4 persons serving on its board of directors.
# Golden Label: entailment

persons_board_premise = 8
persons_board_hypothesis = 4

# the hypothesis refers to the number of persons serving in the board of directors of charities
if persons_board_premise <= persons_board_hypothesis:
    # check if the number of persons in the board according to the premise contradicts the estimate of more than 'persons_board_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
