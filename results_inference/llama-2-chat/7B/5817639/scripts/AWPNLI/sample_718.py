visited_friday_premise = 1250
visited_saturday_premise = 3 * visited_friday_premise
visited_hypothesis = 416.666666667

# check if the number of visitors on Saturday contradicts the estimate from the premise
if visited_hypothesis!= visited_saturday_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
