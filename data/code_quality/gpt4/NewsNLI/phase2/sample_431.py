towns_premise = 32
cities_premise = 2
towns_hypothesis = 32
cities_hypothesis = 2

# the hypothesis mentions the flooding of 32 towns and two cities, which is also mentioned in the premise
if towns_hypothesis != towns_premise:
    # check if the number of towns in the hypothesis contradicts the number of towns reported in the premise
    label = "contradiction"
elif cities_hypothesis != cities_premise:
    # check if the number of cities from the hypothesis contradicts the number of cities in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
