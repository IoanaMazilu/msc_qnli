# Premise: If less than 71 people have visited both Iceland and Norway, how many people have visited neither country?
# Hypothesis: If 51 people have visited both Iceland and Norway, how many people have visited neither country?
# Golden Label: neutral

people_visited_both_premise = 71
people_visited_both_hypothesis = 51

# the hypothesis refers to the number of people who visited both countries mentioned in the premise
if people_visited_both_hypothesis >= people_visited_both_premise:
    # check if the number of people in hypothesis contradicts the estimate of less than 'people_visited_both_premise'
    label = "contradiction"
elif people_visited_both_hypothesis < people_visited_both_premise:
    # if the number of people in the hypothesis is less than the premise, it can be inferred from the premise
    label = "entailment"

print(label)

