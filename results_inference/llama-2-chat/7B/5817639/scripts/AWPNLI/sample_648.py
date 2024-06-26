pounds_premise = 45.0
bags_premise = 1.95652173913

# the hypothesis talks about the number of bags, which is also mentioned in the premise
# compute the total number of pounds of oranges in the premise
total_pounds_premise = pounds_premise * bags_premise

# compare the hypothesis value to the estimate from the premise
if total_pounds_hypothesis!= total_pounds_premise:
    # check if the number of bags from the hypothesis contradicts the estimate of bags from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
