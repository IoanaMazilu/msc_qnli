people_visited_both_premise = 31
people_visited_both_hypothesis = 41

# the hypothesis refers to the number of people visited both countries mentioned in the premise
if people_visited_both_hypothesis <= people_visited_both_premise:
    # check if the hypothetical number contradicts the number of people in the premise
    label = "contradiction"
elif people_visited_both_hypothesis > people_visited_both_premise:
    # if the hypothetical number does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
