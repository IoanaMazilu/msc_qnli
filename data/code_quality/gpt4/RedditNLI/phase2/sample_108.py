payrolls_rise_premise = 164000
payrolls_rise_hypothesis = 164000
jobless_rate_premise = 3.9
jobless_rate_hypothesis = 3.9

# the hypothesis and premise both mention the rise in U.S. payrolls and the jobless rate
if payrolls_rise_hypothesis != payrolls_rise_premise:
    # check if the rise in U.S. payrolls in the hypothesis contradicts the rise in U.S. payrolls in the premise
    label = "contradiction"
elif jobless_rate_hypothesis != jobless_rate_premise:
    # check if the jobless rate in the hypothesis contradicts the jobless rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
