premise_14_boys = 80
premise_15_boys = 70
premise_13_boys = 50
premise_12_boys = 60

hypothesis_14_boys = 50
hypothesis_15_boys = 70
hypothesis_13_boys = 50
hypothesis_12_boys = 60

# check if the hypothesis values contradict the premise values
if hypothesis_14_boys!= premise_14_boys:
    label = "contradiction"
elif hypothesis_15_boys!= premise_15_boys:
    label = "contradiction"
elif hypothesis_13_boys!= premise_13_boys:
    label = "contradiction"
elif hypothesis_12_boys!= premise_12_boys:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
