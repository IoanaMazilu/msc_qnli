work_days_premise = 40
work_days_hypothesis = 20

# the hypothesis refers to the number of days Kamal will take to complete work, which is also mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_days_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise estimate, we can infer entailment
    label = "entailment"

print(label)
