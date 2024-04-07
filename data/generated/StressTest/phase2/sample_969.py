# Premise: Jake can dig a well in 16 days.
# Hypothesis: Jake can dig a well in less than 66 days.
# Golden Label: entailment

dig_days_premise = 16
dig_days_hypothesis = 66

# the hypothesis refers to the number of days Jake needs to dig a well, which is also mentioned in the premise
if dig_days_premise >= dig_days_hypothesis:
    # check if the number of days in the premise contradicts the estimate of less than 'dig_days_hypothesis'
    label = "contradiction"
else:
    # if the number of days in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)

