initial_quarters_premise = 783.0
borrowed_quarters_premise = 271.0
remaining_quarters_hypothesis = 512.0

# the hypothesis refers to the number of quarters Sara has now, which is also calculated in the premise
# calculate the remaining quarters in the premise after her dad borrowed some
remaining_quarters_premise = initial_quarters_premise - borrowed_quarters_premise
if remaining_quarters_hypothesis != remaining_quarters_premise:
    # check if the number of remaining quarters in the hypothesis contradicts the number of remaining quarters from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
