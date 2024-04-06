# Premise: There are 261.0 fish and each fishbowl has 23.0 fish.
# Hypothesis: 11.347826087 fishbowls are there.
# Golden Label: entailment

total_fish_premise = 261.0
fish_per_bowl_premise = 23.0
total_bowls_hypothesis = 11.347826087

# the hypothesis refers to the number of fishbowls, which can be inferred from the premise by dividing the total number of fish by the number of fish per bowl
total_bowls_premise = total_fish_premise / fish_per_bowl_premise

if total_bowls_hypothesis != total_bowls_premise:
    # check if the number of fishbowls in the hypothesis contradicts the number of fishbowls from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"   

print(label)

