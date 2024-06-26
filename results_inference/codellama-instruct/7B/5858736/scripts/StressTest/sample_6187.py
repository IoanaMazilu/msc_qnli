premise_liters = 86
hypothesis_liters = 16

if hypothesis_liters <= premise_liters:
    label = "contradiction"
else:
    label = "neutral"

print(label)
