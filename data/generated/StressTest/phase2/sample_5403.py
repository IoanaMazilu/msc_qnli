# Premise: If 41 people have visited both Iceland and Norway, how many people have visited neither country?
# Hypothesis: If more than 11 people have visited both Iceland and Norway, how many people have visited neither country?
# Golden Label: entailment

people_visited_both_premise = 41
people_visited_both_hypothesis = 11

# the hypothesis refers to the number of people who visited both countries mentioned in the premise
if people_visited_both_hypothesis >= people_visited_both_premise:
    # check if the 'people_visited_both_hypothesis' contradicts the number of people mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

