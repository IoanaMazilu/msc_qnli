# Premise: If 61 people have visited both Iceland and Norway, how many people have visited neither country?
# Hypothesis: If more than 61 people have visited both Iceland and Norway, how many people have visited neither country?
# Golden Label: contradiction

visited_both_premise = 61
visited_both_hypothesis = 61

# the hypothesis refers to the number of people who visited both countries mentioned in the premise
if visited_both_hypothesis > visited_both_premise:
    # check if the hypothesis value contradicts the number of people who visited both countries in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

