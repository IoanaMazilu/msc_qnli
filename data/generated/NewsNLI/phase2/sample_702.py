# Premise: In a poll taken after bin Laden's death, more than two-thirds (69 %) said they think of the United States as more of an enemy.
# Hypothesis: Only 12% said they had a positive view of the United States.
# Golden Label: neutral

negative_view_premise = 0.69
positive_view_hypothesis = 0.12

# the hypothesis mentions the percentage of people that have a positive view of the United States
# the premise mentions the percentage of people that see the United States as an enemy, which is a negative view

# check if the positive view in the hypothesis contradicts the negative view reported in the premise
if positive_view_hypothesis > (1 - negative_view_premise):
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer neutrality
    label = "neutral"

print(label)

