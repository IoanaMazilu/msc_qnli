premise_payrolls = 164000
premise_unemployment_rate = 3.9

hypothesis_payrolls = 164000
hypothesis_unemployment_rate = 3.9

# check if the payrolls in the hypothesis contradict the payrolls in the premise
if hypothesis_payrolls!= premise_payrolls:
    label = "contradiction"
elif hypothesis_unemployment_rate!= premise_unemployment_rate:
    # check if the unemployment rate in the hypothesis contradicts the premise unemployment rate
    label = "contradiction"
else:
    # the premise and hypothesis mention the same payrolls and unemployment rate, so we can infer entailment
    label = "entailment"

print(label)
