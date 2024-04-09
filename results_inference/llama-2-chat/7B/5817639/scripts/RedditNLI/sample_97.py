tariffs_premise = 160000000
tariffs_hypothesis = 160000000

# the premise and hypothesis mention the same amount of tariffs to be imposed
if tariffs_hypothesis == tariffs_premise:
    # check if the hypothesis and premise values are consistent with each other
    label = "entailment"
else:
    # if the hypothesis value contradicts the premise value, label is contradiction
    label = "contradiction"

print(label)
