work_days_rohit_premise = 12
work_days_rohit_hypothesis = 22
work_days_rohan_premise = 6
work_days_rohan_hypothesis = 6

# the hypothesis refers to the number of days Rohit and Rohan can complete a work, mentioned in the premise
if work_days_rohit_hypothesis <= work_days_rohit_premise:
    # check if the estimate of 'work_days_rohit_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
elif work_days_rohan_hypothesis!= work_days_rohan_premise:
    # check if the number of work days in the hypothesis contradicts the number of work days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
