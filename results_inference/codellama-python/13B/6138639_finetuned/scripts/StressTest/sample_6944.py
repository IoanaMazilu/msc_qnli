cities_premise = 7
cities_hypothesis = 6

# the hypothesis talks about the number of cities Jill plans to visit, referenced also in the premise
if cities_hypothesis!= cities_premise:
    # check if the number of cities in the hypothesis contradicts the number of cities reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
