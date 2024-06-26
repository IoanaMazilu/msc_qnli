initial_ducks_premise = 13.0
joined_ducks_premise = 20.0
total_ducks_hypothesis = 31.0

# the hypothesis refers to the total number of ducks, which are also mentioned in the premise
# compute the total number of ducks in the premise
total_ducks_premise = initial_ducks_premise + joined_ducks_premise
if total_ducks_hypothesis != total_ducks_premise:
    # check if the total number of ducks in the hypothesis contradicts the total number of ducks from the premise
    label = "contradiction"
else:
    # if the hypothesis values does not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
