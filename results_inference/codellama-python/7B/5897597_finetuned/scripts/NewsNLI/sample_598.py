elevation_premise = 1000
elevation_hypothesis = 1000
population_hypothesis = 2000000

# the hypothesis mentions the elevation of Lesotho and its population, which are also mentioned in the premise
if elevation_hypothesis!= elevation_premise:
    # check if the elevation in the hypothesis contradicts the elevation reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
