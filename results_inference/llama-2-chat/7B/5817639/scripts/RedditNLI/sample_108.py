premise_payrolls = 164000
premise_jobless_rate = 3.9

# the premise gives the number of payrolls and the jobless rate
if premise_payrolls!= hypothesis_payrolls:
    # check if the number of payrolls in the hypothesis contradicts the number of payrolls in the premise
    label = "contradiction"
elif hypothesis_jobless_rate < min_jobless_rate_premise:
    # check if the estimated jobless rate in the hypothesis contradicts the premise estimate of more than 'jobless_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of payrolls and the jobless rate
    # any estimate of the number of payrolls or jobless rate in the hypothesis consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
