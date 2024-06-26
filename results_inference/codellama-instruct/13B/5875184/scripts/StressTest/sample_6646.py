premise_passengers = 7/12
hypothesis_passengers = 1/12

if premise_passengers <= hypothesis_passengers:
    label = "contradiction"
else:
    label = "neutral"

print(label)
