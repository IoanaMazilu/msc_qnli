# Premise: In a shop, less than 80% socks are white and rest are black.
# Hypothesis: In a shop, 40% socks are white and rest are black.
# Golden Label: neutral

white_socks_premise = 80
white_socks_hypothesis = 40

# The hypothesis refers to the percentage of white socks in the shop mentioned in the premise
if white_socks_hypothesis >= white_socks_premise:
    # Check if the percentage of white socks in the hypothesis contradicts the estimate of less than 'white_socks_premise' in the premise
    label = "contradiction"
else:
    # If the hypothesis value does not contradict the premise one, it can be inferred that it is entailed from the premise
    label = "entailment"

print(label)

