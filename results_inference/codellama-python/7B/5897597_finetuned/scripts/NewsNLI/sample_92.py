workers_premise = 4
workers_hypothesis = 4

# the hypothesis mentions the number of workers in serious condition, which is also referenced in the premise
if workers_hypothesis!= workers_premise:
    # check if the number of workers in the hypothesis contradicts the number of workers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
