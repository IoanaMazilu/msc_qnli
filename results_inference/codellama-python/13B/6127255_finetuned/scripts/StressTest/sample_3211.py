work_days_premise = 40
work_days_hypothesis = 20
rajesh_work_days_premise = 30
rajesh_work_days_hypothesis = 30

# the hypothesis talks about the number of days the unnamed person and Rajesh worked, referenced also in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_days_premise'
    label = "contradiction"
elif rajesh_work_days_hypothesis!= rajesh_work_days_premise:
    # check if the number of days Rajesh worked in the hypothesis contradicts the number of days Rajesh worked reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days the unnamed person worked
    # any number of days less than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)