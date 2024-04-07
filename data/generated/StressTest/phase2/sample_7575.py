# Premise: Sreedhar and Sravan together can do a work in 25 days.
# Hypothesis: Sreedhar and Sravan together can do a work in less than 35 days.
# Golden Label: entailment

work_days_premise = 25
work_days_hypothesis = 35

# the hypothesis refers to the number of days that Sreedhar and Sravan work together, as mentioned in the premise
if work_days_hypothesis < work_days_premise:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
elif work_days_premise > work_days_hypothesis:
    # check if the number of work days in the premise contradicts the number of work days in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

