work_days_alone_premise = 75
work_days_alone_hypothesis = 25

# the hypothesis refers to the number of days Sreedhar alone can do the work, which is also mentioned in the premise
if work_days_alone_hypothesis <= work_days_alone_premise:
    # check if the estimate of 'work_days_alone_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
elif work_days_alone_hypothesis > work_days_alone_premise:
    # check if the number of work days in the hypothesis is greater than the number of work days in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
