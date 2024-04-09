oil_leaked_premise = 6522.0 - 5165.0
hypothesis_oil = 1358.0

# compute the difference between the premise and hypothesis values
diff = oil_leaked_premise - hypothesis_oil

if diff > 0:
    # if the difference is positive, the hypothesis contradicts the premise
    label = "contradiction"
elif diff == 0:
    # if the difference is zero, the hypothesis is neutral with respect to the premise
    label = "neutral"
else:
    # if the difference is negative, the hypothesis entails the premise
    label = "entailment"

print(label)
