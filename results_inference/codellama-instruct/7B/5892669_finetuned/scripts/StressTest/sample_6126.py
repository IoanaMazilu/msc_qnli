visited_both_premise = 31
visited_both_hypothesis = 41

# the hypothesis refers to the number of people who have visited both Iceland and Norway, mentioned in the premise
if visited_both_hypothesis <= visited_both_premise:
    # check if the estimate of 'visited_both_hypothesis' contradicts the number of people who visited both countries in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
