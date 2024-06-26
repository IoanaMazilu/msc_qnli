payrolls_premise = 164000
payrolls_hypothesis = 164000
jobless_rate_premise = 3.9
jobless_rate_hypothesis = 3.9

# the hypothesis and premise mention the number of payrolls and the jobless rate
if payrolls_premise!= payrolls_hypothesis:
    # check if the number of payrolls in the hypothesis contradicts the number of payrolls in the premise
    label = "contradiction"
elif jobless_rate_hypothesis!= jobless_rate_premise:
    # check if the jobless rate in the hypothesis contradicts the jobless rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of payrolls
    # any estimate of the number of payrolls in the hypothesis equal to 'payrolls_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
