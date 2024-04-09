dan_work_hours_premise = 3
dan_work_hours_hypothesis = 4

# the hypothesis refers to the number of hours Dan worked, mentioned also in the premise
if dan_work_hours_hypothesis!= dan_work_hours_premise:
    # check if the number of hours Dan worked in the hypothesis contradicts the number of hours Dan worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
