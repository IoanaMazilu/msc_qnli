premise_variables = {
    "CNN": 1,
    "Argentina": 1,
    "Greece": 1,
    "South Korea": 1,
    "Nigeria": 1
}

hypothesis_variables = {
    "South Korea": 1,
    "Nigeria": 1
}

# compare the values of the variables in the hypothesis with the premise
if hypothesis_variables["South Korea"]!= premise_variables["South Korea"] or hypothesis_variables["Nigeria"]!= premise_variables["Nigeria"]:
    label = "contradiction"
else:
    # if the values of the variables in the hypothesis match the values in the premise, we can infer entailment
    label = "entailment"

print(label)
