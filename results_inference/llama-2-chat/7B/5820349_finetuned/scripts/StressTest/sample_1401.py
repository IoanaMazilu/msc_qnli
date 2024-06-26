work_days_sreedhar_premise = 75
work_days_sreedhar_hypothesis = 25

# the hypothesis refers to the number of days Sreedhar can do the work, also mentioned in the premise
if work_days_sreedhar_premise <= work_days_sreedhar_hypothesis:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
