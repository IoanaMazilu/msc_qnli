# Premise: Frank is 13 years younger then John.
# Hypothesis: Frank is less than 63 years younger then John.
# Golden Label: entailment

frank_john_age_diff_premise = 13
frank_john_age_diff_hypothesis = 63

# The hypothesis talks about the age difference between Frank and John, also mentioned in the premise
if frank_john_age_diff_hypothesis < frank_john_age_diff_premise:
    # Check if the hypothesis value contradicts the exact age difference stated in the premise
    label = "contradiction"
else:
    # The hypothesis value is more than the premise one, so it doesn't contradict the premise
    # But since the hypothesis doesn't exactly match the premise, we can't infer entailment
    label = "neutral"

print(label)

