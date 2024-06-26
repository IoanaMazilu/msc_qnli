premise_rainfall = 25
hypothesis_rainfall = 65

if premise_rainfall < hypothesis_rainfall:
    label = "contradiction"
else:
    label = "neutral"

print(label)
