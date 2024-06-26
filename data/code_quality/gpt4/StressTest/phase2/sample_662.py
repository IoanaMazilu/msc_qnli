rosy_efficiency_premise = 40
rosy_efficiency_hypothesis = 30

# the hypothesis talks about Rosy's efficiency compared to Mary's, referenced also in the premise
if rosy_efficiency_hypothesis != rosy_efficiency_premise:
    # check if the hypothesis value contradicts the efficiency difference mentioned in the premise
    label = "contradiction"
else:
    # the efficiency difference values in the hypothesis and the premise are the same
    label = "entailment"

print(label)
