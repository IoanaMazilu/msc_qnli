# Premise: Anita has 360 apples.
# Hypothesis: Anita has 560 apples.
# Golden Label: contradiction

apples_premise = 360
apples_hypothesis = 560

# the hypothesis refers to the number of apples Anita has, which is also mentioned in the premise
if apples_hypothesis == apples_premise:
    # check if the number of apples in the hypothesis is the same as in the premise
    label = "entailment"
else:
    # any other number of apples in the hypothesis contradicts the number in the premise
    label = "contradiction"

print(label)

