payrolls_gain_premise = 164000
payrolls_gain_hypothesis = 164000
jobless_rate_premise = 3.9
jobless_rate_hypothesis = 3.9

# the hypothesis and premise mention the gain in payrolls and the jobless rate
if payrolls_gain_premise!= payrolls_gain_hypothesis:
    # check if the payrolls gain in the hypothesis contradicts the payrolls gain in the premise
    label = "contradiction"
elif jobless_rate_premise!= jobless_rate_hypothesis:
    # check if the jobless rate in the hypothesis contradicts the jobless rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
