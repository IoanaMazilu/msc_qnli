people_visited_both_premise = 31
people_visited_both_hypothesis = 41

# the hypothesis refers to the number of people who visited both countries, mentioned in the premise
if people_visited_both_premise >= people_visited_both_hypothesis:
    # check if the estimate of 'people_visited_both_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
