cigarettes_per_case_premise = 8
cigarettes_per_case_hypothesis = 5
cases_per_2_hours_premise = 2
cases_per_2_hours_hypothesis = 2

# the hypothesis refers to the number of cigarettes per case and the number of cases packed per 2 hours, both mentioned in the premise
if cigarettes_per_case_premise <= cigarettes_per_case_hypothesis:
    # check if the estimate of 'cigarettes_per_case_hypothesis' contradicts the number of cigarettes per case in the premise
    label = "contradiction"
elif cases_per_2_hours_hypothesis!= cases_per_2_hours_premise:
    # check if the number of cases packed per 2 hours in the hypothesis contradicts the number of cases packed per 2 hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
