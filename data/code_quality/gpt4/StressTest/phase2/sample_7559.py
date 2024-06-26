pairs_shoes_marcella_premise = 25
pairs_shoes_marcella_hypothesis = 25

# the hypothesis refers to the number of pairs of shoes Marcella has, mentioned in the premise
if pairs_shoes_marcella_hypothesis < pairs_shoes_marcella_premise:
    # check if the number of pairs of shoes in the hypothesis is less than the number reported in the premise
    label = "entailment"
else:
    # if the hypothesis value is not less than the premise one, we can infer contradiction
    label = "contradiction"

print(label)
