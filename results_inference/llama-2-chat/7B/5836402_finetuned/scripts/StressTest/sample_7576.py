total_days_premise = 35
total_days_hypothesis = 25

# the hypothesis refers to the number of days needed for Sreedhar and Sravan to complete a work, which is also mentioned in the premise
if total_days_hypothesis >= total_days_premise:
    # check if the estimate of 'total_days_hypothesis' contradicts the number of days mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
