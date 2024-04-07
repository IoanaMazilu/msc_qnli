# Premise: In a shop, 40% socks are white and rest are black.
# Hypothesis: In a shop, 10% socks are white and rest are black.
# Golden Label: contradiction

white_socks_premise = 40
white_socks_hypothesis = 10

# the hypothesis refers to the percentage of white socks mentioned in the premise
if white_socks_hypothesis != white_socks_premise:
    # check if the percentage of white socks in the hypothesis contradicts the percentage of white socks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

