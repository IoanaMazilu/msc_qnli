payrolls_gain_premise = 164000
payrolls_gain_hypothesis = 164000
jobless_rate_premise = 3.9
jobless_rate_hypothesis = 3.9

# the hypothesis and premise mention the number of payrolls gain and the jobless rate in the US
if payrolls_gain_hypothesis!= payrolls_gain_premise:
    # check if the number of payrolls gain in the hypothesis contradicts the number of payrolls gain in the premise
    label = "contradiction"
elif jobless_rate_hypothesis!= jobless_rate_premise:
    # check if the jobless rate in the hypothesis contradicts the jobless rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
