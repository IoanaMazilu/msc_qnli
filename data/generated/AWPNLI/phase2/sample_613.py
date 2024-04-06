# Premise: There are 261.0 fish and each fishbowl has 23.0 fish.
# Hypothesis: 12.5 fishbowls are there.
# Golden Label: contradiction

total_fish_premise = 261.0
fish_per_bowl_premise = 23.0
fishbowls_hypothesis = 12.5

# the hypothesis refers to the total number of fishbowls, which can be inferred from the premise 
# compute the total number of fishbowls in the premise
fishbowls_premise = total_fish_premise / fish_per_bowl_premise
if fishbowls_hypothesis != fishbowls_premise:
    # check if the number of fishbowls in the hypothesis contradicts the number of fishbowls from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

