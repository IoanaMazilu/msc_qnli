rosy_efficiency_premise = 30
rosy_efficiency_hypothesis = 10

# the hypothesis refers to Rosy's efficiency in comparison to Mary's, which is also discussed in the premise
if rosy_efficiency_hypothesis > rosy_efficiency_premise:
    # check if the 'rosy_efficiency_hypothesis' contradicts the maximum value for Rosy's efficiency in the premise
    label = "contradiction"
elif rosy_efficiency_hypothesis < rosy_efficiency_premise:
    # if Rosy's efficiency in the hypothesis is less than the maximum efficiency in the premise, we can infer entailment
    label = "entailment"
else:
    # if the efficiency in the hypothesis equals the maximum efficiency in the premise, we can infer entailment
    label = "entailment"

print(label)
