# Premise: He works at it for 20 days and then Rajesh finished it in 30 days.
# Hypothesis: He works at it for 70 days and then Rajesh finished it in 30 days.
# Golden Label: contradiction

he_work_days_premise = 20
he_work_days_hypothesis = 70
rajesh_work_days_premise = 30
rajesh_work_days_hypothesis = 30

# the hypothesis refers to the number of days he and Rajesh worked, mentioned in the premise
if rajesh_work_days_hypothesis != rajesh_work_days_premise:
    # check if the number of days Rajesh worked in the hypothesis contradicts the number of days Rajesh worked reported in the premise
    label = "contradiction"
elif he_work_days_hypothesis != he_work_days_premise:
    # check if the number of days he worked in the hypothesis contradicts the number of days he worked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

