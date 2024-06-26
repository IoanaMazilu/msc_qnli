raj_age_future_premise = 32
raj_age_future_hypothesis = 12

# The hypothesis refers to Raj's age in the future, also mentioned in the premise
if raj_age_future_premise != raj_age_future_hypothesis:
    # Check if the predicted age of Raj in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis value does not contradict the premise value, then it is either entailment or neutral
    # But in this case, the premise does not give any specific value for the age of Raj's parents, so any age can be neutral
    label = "neutral"

print(label)
