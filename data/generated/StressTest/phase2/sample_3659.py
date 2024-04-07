# Premise: If 51 people have visited both Iceland and Norway, how many people have visited neither country?
# Hypothesis: If 81 people have visited both Iceland and Norway, how many people have visited neither country?
# Golden Label: contradiction

people_visited_both_premise = 51
people_visited_both_hypothesis = 81

# the hypothesis talks about the number of people who visited both countries, referenced also in the premise
if people_visited_both_hypothesis != people_visited_both_premise:
    # check if the number of people visiting both in the hypothesis contradicts the number of people visiting both reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

