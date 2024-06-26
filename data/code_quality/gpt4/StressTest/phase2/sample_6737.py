rohit_work_days_premise = 12
rohan_work_days_premise = 6
rohit_work_days_hypothesis = 62
rohan_work_days_hypothesis = 6

# The hypothesis refers to the time Rohit and Rohan can complete a work, which is mentioned in the premise.
if rohit_work_days_hypothesis != rohit_work_days_premise:
    # Check if the work days for Rohit in the hypothesis contradicts the work days for Rohit reported in the premise.
    label = "contradiction"
elif rohan_work_days_hypothesis != rohan_work_days_premise:
    # Check if the work days for Rohan in the hypothesis contradicts the work days for Rohan reported in the premise.
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment.
    label = "entailment"

print(label)
