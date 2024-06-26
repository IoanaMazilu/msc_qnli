oil_premise = 6522.0
leaked_premise = 5165.0
hypothesis = 1357.0

# compute the difference between the premise and hypothesis
diff = hypothesis - leaked_premise

# check if the difference is positive
if diff > 0:
    # if the difference is positive, the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the difference is zero or negative, the hypothesis is neutral or entails the premise
    label = "entailment"

print(label)
