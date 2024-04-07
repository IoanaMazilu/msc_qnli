# Premise: The next day, Bob took the test, and with this grade included, the new average was 78.
# Hypothesis: The next day, Bob took the test, and with this grade included, the new average was less than 78.
# Golden Label: contradiction

average_score_premise = 78
average_score_hypothesis = 78

# the hypothesis talks about the average score after Bob's test, which is also referenced in the premise
if average_score_hypothesis >= average_score_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif average_score_hypothesis < average_score_premise:
    # if the hypothesis value is less than the premise one, we can infer entailment
    label = "entailment"

print(label)

