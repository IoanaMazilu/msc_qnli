ravi_work_days_premise = 24
prakash_work_days_premise = 40
ravi_work_days_hypothesis = 74
prakash_work_days_hypothesis = 40

# The hypothesis refers to the number of days Ravi and Prakash need to complete a piece of work, 
# which is also mentioned in the premise
if ravi_work_days_hypothesis != ravi_work_days_premise:
    # Check if the number of days Ravi needs to complete a piece of work in the hypothesis contradicts 
    # the number of days mentioned in the premise
    label = "contradiction"
elif prakash_work_days_hypothesis != prakash_work_days_premise:
    # Check if the number of days Prakash needs to complete a piece of work in the hypothesis contradicts 
    # the number of days mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
