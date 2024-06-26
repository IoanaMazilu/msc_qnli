workers_serious_condition_premise = 4
workers_serious_condition_hypothesis = 4

# the hypothesis mentions the number of workers in serious condition, which is also referenced in the premise
if workers_serious_condition_hypothesis!= workers_serious_condition_premise:
    # check if the number of workers in serious condition in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
