hours_paid_x_premise = 40
hours_paid_x_hypothesis = 50

# the hypothesis refers to the number of hours James is paid x dollars per hour, mentioned in the premise
if hours_paid_x_hypothesis!= hours_paid_x_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
