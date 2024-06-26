yhat_premise = 5
yhat_hypothesis = 3

# The hypothesis talks about the number of people taken to hospitals, which is also referenced in the premise
if yhat_hypothesis!= yhat_premise:
    # Check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # If the number of people in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
