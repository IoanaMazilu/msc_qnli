# define variables for the number of hours worked per day and the days of the week
monday_work_premise = 8
wednesday_work_premise = 8
friday_work_premise = 8
tuesday_work_premise = 6
thursday_work_premise = 6

monday_work_hypothesis = 5
wednesday_work_hypothesis = 5
friday_work_hypothesis = 5
tuesday_work_hypothesis = 6
thursday_work_hypothesis = 6

# the hypothesis refers to the number of hours worked per day and the days of the week mentioned in the premise
if monday_work_hypothesis >= monday_work_premise and wednesday_work_hypothesis >= wednesday_work_premise and friday_work_hypothesis >= friday_work_premise:
    # check if the number of hours worked per day in the hypothesis contradicts the number of hours worked per day in the premise
    label = "contradiction"
elif tuesday_work_hypothesis!= tuesday_work_premise or thursday_work_hypothesis!= thursday_work_premise:
    # check if the number of hours worked per day in the hypothesis contradicts the number of hours worked per day in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
