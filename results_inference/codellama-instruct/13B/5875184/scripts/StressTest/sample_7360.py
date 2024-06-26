premise_boys_14 = 20
premise_boys_15 = 70
premise_boys_13 = 50
premise_boys_12 = 60

hypothesis_boys_14 = 80
hypothesis_boys_15 = 70
hypothesis_boys_13 = 50
hypothesis_boys_12 = 60

# check if the hypothesis values contradict the premise estimates
if hypothesis_boys_14 > premise_boys_14:
    label = "contradiction"
elif hypothesis_boys_15 > premise_boys_15:
    label = "contradiction"
elif hypothesis_boys_13 > premise_boys_13:
    label = "contradiction"
elif hypothesis_boys_12 > premise_boys_12:
    label = "contradiction"
else:
    label = "neutral"

print(label)
