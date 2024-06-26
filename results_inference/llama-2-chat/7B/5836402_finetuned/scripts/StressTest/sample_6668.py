work_days_premise = 20
work_days_hypothesis = 50

# the hypothesis refers to the number of days Kamal will take to complete the work mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the estimate of 'work_days_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than 'work_days_premise', it is not possible to complete the work in that number of days
    # therefore, the hypothesis cannot be entailed from the premise
    label = "neutral"

print(label)
