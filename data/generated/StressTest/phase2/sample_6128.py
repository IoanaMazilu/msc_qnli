# Premise: If 31 people have visited both Iceland and Norway, how many people have visited neither country?
# Hypothesis: If less than 31 people have visited both Iceland and Norway, how many people have visited neither country?
# Golden Label: contradiction

people_visited_both_premise = 31
people_visited_both_hypothesis = 31

# the hypothesis refers to the number of people who visited both countries, which is also mentioned in the premise
if people_visited_both_hypothesis < people_visited_both_premise:
    # check if the hypothesis value contradicts the number of people visited both countries in the premise
    label = "contradiction"
elif people_visited_both_hypothesis == people_visited_both_premise:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

