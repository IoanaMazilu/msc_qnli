cities_visited_premise = 7
cities_visited_hypothesis = 6

# the hypothesis talks about the number of cities visited by Jill, referenced also in the premise
if cities_visited_hypothesis!= cities_visited_premise:
    # check if the number of cities visited in the hypothesis contradicts the number of cities visited reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
