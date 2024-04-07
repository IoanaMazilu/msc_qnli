# Premise: Mary works in a restaurant a maximum of 50 hours.
# Hypothesis: Mary works in a restaurant a maximum of less than 60 hours.
# Golden Label: entailment

max_work_hours_premise = 50
max_work_hours_hypothesis = 60

# the hypothesis refers to the maximum number of hours Mary works in a restaurant, mentioned also in the premise
if max_work_hours_hypothesis <= max_work_hours_premise:
    # check if the estimate of 'max_work_hours_hypothesis' contradicts the maximum number of work hours in the premise
    label = "contradiction"
elif max_work_hours_premise != max_work_hours_hypothesis:
    # check if the maximum number of work hours in the hypothesis contradicts the maximum number of work hours mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

