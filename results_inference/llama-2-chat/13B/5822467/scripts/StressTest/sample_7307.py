monday_hours_premise = 9
monday_hours_hypothesis = 5
wednesday_hours_premise = 9
wednesday_hours_hypothesis = 5
friday_hours_premise = 9
friday_hours_hypothesis = 5
tuesday_hours_premise = 5
tuesday_hours_hypothesis = 5
thursday_hours_premise = 5
thursday_hours_hypothesis = 5

# the hypothesis refers to the number of hours Mary works on each day
if monday_hours_premise <= monday_hours_hypothesis:
    # check if the estimate of'monday_hours_hypothesis' contradicts the number of hours Mary works on Monday in the premise
    label = "contradiction"
elif wednesday_hours_hypothesis!= wednesday_hours_premise:
    # check if the number of hours Mary works on Wednesday in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
elif friday_hours_hypothesis!= friday_hours_premise:
    # check if the number of hours Mary works on Friday in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
