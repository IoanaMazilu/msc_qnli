payrolls_premise = 164000
payrolls_hypothesis = 164000
jobless_rate_premise = 3.9
jobless_rate_hypothesis = 3.9

# the hypothesis mentions the same payrolls and jobless rate as the premise
if payrolls_hypothesis!= payrolls_premise:
    # check if the payrolls in the hypothesis contradict the payrolls in the premise
    label = "contradiction"
elif jobless_rate_hypothesis!= jobless_rate_premise:
    # check if the jobless rate in the hypothesis contradicts the jobless rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
