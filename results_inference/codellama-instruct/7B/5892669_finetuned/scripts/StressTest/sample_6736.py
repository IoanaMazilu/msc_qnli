rohit_work_days_premise = 22
rohan_work_days_premise = 6
rohit_work_days_hypothesis = 12
rohan_work_days_hypothesis = 6

# the hypothesis refers to the number of days Rohit and Rohan need to complete a work, mentioned in the premise
if rohit_work_days_hypothesis >= rohit_work_days_premise:
    # check if the estimate of 'rohit_work_days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
elif rohan_work_days_hypothesis!= rohan_work_days_premise:
    # check if the number of days Rohan needs in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Rohit needs
    # any number of days less than 'rohit_work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
