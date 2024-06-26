lower_bound_premise = 5
upper_bound_premise = 10
lower_bound_hypothesis = 5
upper_bound_hypothesis = 10

# the hypothesis talks about the percentage of stolen artworks that get returned, which is also mentioned in the premise
if lower_bound_hypothesis!= lower_bound_premise or upper_bound_hypothesis!= upper_bound_premise:
    # check if the lower and upper bounds of the percentage in the hypothesis contradict the ones from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
