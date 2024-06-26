stations_premise = 18
stations_hypothesis = 18

# the hypothesis refers to the number of stations between Hyderabad and Bangalore mentioned in the premise
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the exact number of stations in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
