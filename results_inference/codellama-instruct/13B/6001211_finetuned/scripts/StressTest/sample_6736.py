rohit_work_days_premise = 22
rohit_work_days_hypothesis = 12
rohan_work_days_premise = 6
rohan_work_days_hypothesis = 6

# the hypothesis refers to the number of days Rohit and Rohan can complete a work, mentioned in the premise
if rohit_work_days_hypothesis >= rohit_work_days_premise:
    # check if the number of days in the hypothesis contradicts the estimate of less than 'rohit_work_days_premise'
    label = "contradiction"
elif rohan_work_days_hypothesis!= rohan_work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Rohit can complete a work
    # any number of days less than 'rohit_work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
