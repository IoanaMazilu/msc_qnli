fish_premise = 49.0
more_fish_premise = 18.0
marbles_hypothesis = 67.0

# the hypothesis refers to the number of marbles, which are not mentioned in the premise
# compute the total number of fish in the premise
total_fish_premise = fish_premise + more_fish_premise
if total_fish_premise!= marbles_hypothesis:
    # check if the number of marbles in the hypothesis contradicts the number of fish from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
