# Premise: He works at it for 20 days and then Rajesh finished it in 30 days.
# Hypothesis: He works at it for less than 40 days and then Rajesh finished it in 30 days.
# Golden Label: entailment

work_days_premise = 20
work_days_hypothesis = 40
rajesh_work_days_premise = 30
rajesh_work_days_hypothesis = 30

# the hypothesis is about the number of days he works, and the number of days Rajesh works, both mentioned in the premise
if work_days_premise >= work_days_hypothesis:
    # check if the 'work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
elif rajesh_work_days_hypothesis != rajesh_work_days_premise:
    # check if the number of work days Rajesh in the hypothesis contradicts the number of work days Rajesh reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

