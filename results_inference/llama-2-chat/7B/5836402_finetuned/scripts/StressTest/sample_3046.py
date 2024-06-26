work_hours_premise = [5, 6, 6, 6]
work_hours_hypothesis = [8, 6, 6, 6]

# the hypothesis refers to the number of hours Sheila works per day, which is also mentioned in the premise
for day in range(len(work_hours_premise)):
    if work_hours_premise[day]!= work_hours_hypothesis[day]:
        # check if the number of hours Sheila works on each day in the hypothesis contradicts the number of hours reported in the premise
        label = "contradiction"
        break
    else:
        # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
        label = "entailment"
        break

print(label)
