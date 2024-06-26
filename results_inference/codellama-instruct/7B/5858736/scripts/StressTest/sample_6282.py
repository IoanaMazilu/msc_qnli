# Define variables for the premise and hypothesis
robin_test_score_premise = 82
robin_test_score_hypothesis = 82

# Check if the hypothesis value contradicts the premise value
if robin_test_score_hypothesis!= robin_test_score_premise:
    label = "contradiction"
else:
    # If the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
