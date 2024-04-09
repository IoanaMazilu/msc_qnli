cigarettes_per_case_premise = 5
cigarettes_per_case_hypothesis = 1

# the hypothesis refers to the number of cigarettes per case mentioned in the premise
if cigarettes_per_case_premise!= cigarettes_per_case_hypothesis:
    # check if the number of cigarettes per case in the hypothesis contradicts the number of cigarettes per case reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
