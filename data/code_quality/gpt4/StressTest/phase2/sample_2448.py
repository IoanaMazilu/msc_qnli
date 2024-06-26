diana_age_diff_premise = 4
diana_age_diff_hypothesis = 3

# the hypothesis refers to the age difference between Diana and Rashid mentioned in the premise
if diana_age_diff_premise < diana_age_diff_hypothesis:
    # check if the age difference in the premise contradicts the hypothesis
    label = "contradiction"
elif diana_age_diff_premise > diana_age_diff_hypothesis:
    # check if the age difference in the premise entails the hypothesis
    label = "entailment"
else:
    # if neither contradiction nor entailment can be inferred, the relation is neutral
    label = "neutral"

print(label)
