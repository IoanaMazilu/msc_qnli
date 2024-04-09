work_days_rohit_premise = 22
work_days_rohan_premise = 6
work_days_rohit_hypothesis = 12
work_days_rohan_hypothesis = 6

# the hypothesis refers to the number of days Rohit and Rohan can complete a work, as mentioned in the premise
if work_days_rohit_hypothesis >= work_days_rohit_premise:
    # check if the estimate of 'work_days_rohit_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
elif work_days_rohan_hypothesis!= work_days_rohan_premise:
    # check if the number of work days for Rohan in the hypothesis contradicts the number of work days reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of work days for Rohit
    # any number of work days less than 'work_days_rohit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
