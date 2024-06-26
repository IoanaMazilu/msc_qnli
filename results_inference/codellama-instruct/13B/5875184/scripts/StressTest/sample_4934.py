premise_days = [18, 27, 36]
hypothesis_days = [58, 27, 36]

# check if the hypothesis values contradict the premise ones
if hypothesis_days[0] <= premise_days[0]:
    label = "contradiction"
elif hypothesis_days[1]!= premise_days[1]:
    label = "contradiction"
elif hypothesis_days[2]!= premise_days[2]:
    label = "contradiction"
else:
    label = "neutral"

print(label)
