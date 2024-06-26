premise_payrolls = 164000
hypothesis_payrolls = 164000
premise_jobless_rate = 3.9
hypothesis_jobless_rate = 3.9

# the hypothesis and premise mention the number of payrolls and jobless rate
if premise_payrolls!= hypothesis_payrolls:
    # check if the number of payrolls in the hypothesis contradicts the number of payrolls in the premise
    label = "contradiction"
elif premise_jobless_rate!= hypothesis_jobless_rate:
    # check if the jobless rate in the hypothesis contradicts the jobless rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
