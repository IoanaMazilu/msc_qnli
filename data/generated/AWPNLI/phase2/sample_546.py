# Premise: Mrs. Sheridan has 47.0 fish and she gave her sister 22.0 fish.
# Hypothesis: She has 25.0 fish now.
# Golden Label: entailment

initial_fish_premise = 47.0
given_fish_premise = 22.0
remaining_fish_hypothesis = 25.0

# the hypothesis refers to the number of fish Mrs. Sheridan has now, which are also mentioned in the premise
# compute the remaining number of fish in the premise
remaining_fish_premise = initial_fish_premise - given_fish_premise
if remaining_fish_hypothesis != remaining_fish_premise:
    # check if the remaining number of fish in the hypothesis contradicts the remaining number of fish from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

