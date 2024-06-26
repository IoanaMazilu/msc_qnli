fish_premise = 49.0
given_fish_premise = 18.0
total_fish_hypothesis = 67.0

# the hypothesis refers to the number of marbles, which are not mentioned in the premise
# the premise gives the number of fish Michael has and the number of additional fish given by Ben
# compute the total number of fish in the premise
total_fish_premise = fish_premise + given_fish_premise
if total_fish_hypothesis!= total_fish_premise:
    # check if the number of marbles in the hypothesis contradicts the number of fish from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
