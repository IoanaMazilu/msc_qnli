son_life_premise = 1/2
son_life_hypothesis = 5/2

# the hypothesis refers to the son's life span compared to Adam's, also mentioned in the premise
if son_life_hypothesis == son_life_premise:
    # check if the ratio of 'son_life_hypothesis' contradicts the ratio of son's life to Adam's life in the premise
    label = "entailment"
else:
    # if the hypothesis ratio does not match the premise ratio, we can infer contradiction
    label = "contradiction"

print(label)
