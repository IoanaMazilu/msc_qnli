cigarettes_per_case_premise = 5
cigarettes_per_case_hypothesis = 8

# the hypothesis refers to the number of cigarettes per case mentioned in the premise
if cigarettes_per_case_hypothesis <= cigarettes_per_case_premise:
    # check if the estimate of 'cigarettes_per_case_hypothesis' contradicts the number of cigarettes per case in the premise
    label = "contradiction"
elif cigarettes_per_case_hypothesis > cigarettes_per_case_premise:
    # check if the number of cigarettes per case in the hypothesis contradicts the number of cigarettes per case reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
