fish_premise = 212.0
fish_hypothesis = 492.0

# the hypothesis refers to the total number of fish, which is also mentioned in the premise
# compute the total number of fish in the premise
total_fish_premise = fish_premise + fish_hypothesis

# check if the hypothesis contradicts the premise
if total_fish_premise!= fish_hypothesis:
    label = "contradiction"
else:
    label = "entailment"

print(label)
