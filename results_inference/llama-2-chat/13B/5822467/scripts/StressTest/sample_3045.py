sheila_work_premise = 8 * 3 + 6 * 2
sheila_work_hypothesis = 5 * 3 + 6 * 2

# the hypothesis refers to the number of hours Sheila works per day, mentioned in the premise
if sheila_work_premise <= sheila_work_hypothesis:
    # check if the estimate of'sheila_work_hypothesis' contradicts the number of hours Sheila works per day in the premise
    label = "contradiction"
elif sheila_work_hypothesis > sheila_work_premise:
    # check if the number of hours Sheila works per day in the hypothesis contradicts the number of hours Sheila works per day reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
