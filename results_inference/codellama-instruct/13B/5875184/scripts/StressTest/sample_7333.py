premise = "In ABC limited, more than 25% are using Samsung phone at the same time 70% using i phone ; If in the same company 85% are using Samsung phone then, what is the percentage of i phone user?"
hypothesis = "In ABC limited, 75% are using Samsung phone at the same time 70% using i phone ; If in the same company 85% are using Samsung phone then, what is the percentage of i phone user?"

# extract the numerical entities from the premise and hypothesis
premise_samsung_percentage = 25
premise_iphone_percentage = 70
hypothesis_samsung_percentage = 75
hypothesis_iphone_percentage = 70

# check if the hypothesis value contradicts the premise value
if hypothesis_samsung_percentage <= premise_samsung_percentage:
    label = "contradiction"
elif hypothesis_iphone_percentage!= premise_iphone_percentage:
    label = "contradiction"
else:
    label = "entailment"

print(label)
