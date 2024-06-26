pink_highlighters_premise = 24
yellow_highlighters_premise = 28
blue_highlighters_premise = 25

pink_highlighters_hypothesis = 24
yellow_highlighters_hypothesis = 28
blue_highlighters_hypothesis = 25

# the hypothesis refers to the number of each color of highlighters mentioned in the premise
if pink_highlighters_hypothesis >= pink_highlighters_premise or yellow_highlighters_hypothesis >= yellow_highlighters_premise or blue_highlighters_hypothesis >= blue_highlighters_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # if the hypothesis values are less than the premise ones, the hypothesis can be inferred from the premise
    label = "entailment"

print(label)
