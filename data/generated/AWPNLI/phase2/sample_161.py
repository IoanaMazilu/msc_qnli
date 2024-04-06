# Premise: Mrs. Sheridan has 22.0 fish and her sister gave her 47.0 more fish.
# Hypothesis: She has 72.0 fish now.
# Golden Label: contradiction

fish_premise = 22.0
fish_received_premise = 47.0
total_fish_hypothesis = 72.0

# the hypothesis refers to the total number of fish, which are also mentioned in the premise
# compute the total number of fish in the premise
total_fish_premise = fish_premise + fish_received_premise
if total_fish_hypothesis != total_fish_premise:
    # check if the total number of fish in the hypothesis contradicts the total number of fish from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

