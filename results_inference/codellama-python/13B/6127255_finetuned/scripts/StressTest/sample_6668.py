#work_days_premise = 20
#work_days_hypothesis = 50

# the hypothesis refers to the number of days Kamal will work, which is also mentioned in the premise
if work_days_hypothesis!= work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days mentioned in the premise
    label = "contradiction"
else:
    # if the number of days in the hypothesis does not contradict the number of days in the premise, we can infer entailment
    label = "entailment"

print(label)
# 