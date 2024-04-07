# Premise: He works at it for less than 60 days and then Rajesh finished it in 30 days.
# Hypothesis: He works at it for 20 days and then Rajesh finished it in 30 days.
# Golden Label: neutral

work_days_premise = 60
work_days_hypothesis = 20
rajesh_work_days_premise = 30
rajesh_work_days_hypothesis = 30

# the hypothesis refers to the number of work days and Rajesh's work days mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
elif rajesh_work_days_hypothesis != rajesh_work_days_premise:
    # check if the number of Rajesh's work days in the hypothesis contradicts the number of Rajesh's work days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

