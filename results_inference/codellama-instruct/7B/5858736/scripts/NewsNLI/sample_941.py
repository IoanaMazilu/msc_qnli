premise_missing_personnel = 18
hypothesis_missing_personnel = 18

if hypothesis_missing_personnel!= premise_missing_personnel:
    label = "contradiction"
else:
    label = "neutral"

print(label)
