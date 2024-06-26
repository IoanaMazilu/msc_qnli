stations_premise = 75
stations_hypothesis = 15

# the hypothesis refers to the number of stations between Hyderabad and Bangalore, which is also mentioned in the premise
if stations_hypothesis >= stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations in the premise
    label = "contradiction"
else:
    # if the number of stations in the hypothesis is less than the number of stations in the premise, we can infer entailment
    label = "entailment"

print(label)
