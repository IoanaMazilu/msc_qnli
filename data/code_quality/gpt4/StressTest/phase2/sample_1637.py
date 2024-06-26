stations_premise = 18
stations_hypothesis = 78

# the hypothesis refers to the number of stations between Hyderabad and Bangalore mentioned in the premise
if stations_hypothesis != stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations in the premise
    label = "contradiction"
else:
    # if the number of stations in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
