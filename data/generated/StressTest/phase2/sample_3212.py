# Premise: He works at it for 20 days and then Rajesh finished it in 30 days.
# Hypothesis: He works at it for 30 days and then Rajesh finished it in 30 days.
# Golden Label: contradiction

work_days_premise = 20
work_days_hypothesis = 30
rajesh_work_days_premise = 30
rajesh_work_days_hypothesis = 30

# the hypothesis talks about the number of days the unnamed person and Rajesh worked, which is also referenced in the premise
if work_days_hypothesis != work_days_premise:
    # check if the number of days the unnamed person worked in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif rajesh_work_days_hypothesis != rajesh_work_days_premise:
    # check if the number of days Rajesh worked in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

