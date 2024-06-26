stations_premise = 75
stations_hypothesis = 15

# the hypothesis refers to the number of stations between Hyderabad and Bangalore, which is also mentioned in the premise
if stations_hypothesis >= stations_premise:
    # check if the number of stations in the hypothesis contradicts the estimate of less than'stations_premise'
    label = "contradiction"
elif stations_hypothesis < stations_premise:
    # check if the number of stations in the hypothesis is less than the number of stations in the premise
    label = "entailment"
else:
    # if the number of stations in the hypothesis is equal to the number of stations in the premise, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
