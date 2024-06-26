visited_neither_premise = 41 - 31
visited_neither_hypothesis = 0

# the hypothesis refers to the number of people who have visited neither country
if visited_neither_premise <= visited_neither_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'visited_neither_premise'
    label = "contradiction"
elif visited_neither_hypothesis!= visited_neither_premise:
    # check if the number of people who have visited neither country in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
