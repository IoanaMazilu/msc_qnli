payrolls_premise = 164000
payrolls_hypothesis = 164000
jobless_rate_premise = 3.9
jobless_rate_hypothesis = 3.9

# the hypothesis and premise mention the payrolls and jobless rate
if payrolls_premise!= payrolls_hypothesis:
    # check if the payrolls in the hypothesis contradicts the payrolls in the premise
    label = "contradiction"
elif jobless_rate_premise!= jobless_rate_hypothesis:
    # check if the jobless rate in the hypothesis contradicts the jobless rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
