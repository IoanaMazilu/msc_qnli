# Premise: If 61 people have visited both Iceland and Norway, how many people have visited neither country?
# Hypothesis: If less than 71 people have visited both Iceland and Norway, how many people have visited neither country?
# Golden Label: entailment

people_visited_both_premise = 61
people_visited_both_hypothesis = 71

# the hypothesis talks about the number of people who have visited both countries, which is also mentioned in the premise
if people_visited_both_hypothesis <= people_visited_both_premise:
    # check if the hypothesis value contradicts the number of people in the premise
    label = "contradiction"
elif people_visited_both_hypothesis > people_visited_both_premise:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

