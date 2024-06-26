stations_between_cities_premise = 10
stations_between_cities_hypothesis = 60

# the hypothesis talks about the number of stations between two cities mentioned in the premise
if stations_between_cities_hypothesis != stations_between_cities_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value matches the premise one, we can infer entailment
    label = "entailment"

print(label)
