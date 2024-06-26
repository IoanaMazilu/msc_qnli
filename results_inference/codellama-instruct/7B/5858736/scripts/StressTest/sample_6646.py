premise_passengers = 7/12
premise_Europeans = 1/4
premise_Africa = 2/9
premise_Asia = 1/6
premise_others = 50/6

hypothesis_passengers = 1/12
hypothesis_Europeans = 1/4
hypothesis_Africa = 2/9
hypothesis_Asia = 1/6
hypothesis_others = 50/6

# check if the hypothesis values contradict the premise ones
if hypothesis_passengers!= premise_passengers:
    label = "contradiction"
elif hypothesis_Europeans!= premise_Europeans:
    label = "contradiction"
elif hypothesis_Africa!= premise_Africa:
    label = "contradiction"
elif hypothesis_Asia!= premise_Asia:
    label = "contradiction"
elif hypothesis_others!= premise_others:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
