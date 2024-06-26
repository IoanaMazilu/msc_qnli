people_visited_both_premise = 21
people_visited_both_hypothesis = 71

# the hypothesis refers to the number of people who visited both countries mentioned in the premise
if people_visited_both_hypothesis < people_visited_both_premise:
    # check if the hypothesis value contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
