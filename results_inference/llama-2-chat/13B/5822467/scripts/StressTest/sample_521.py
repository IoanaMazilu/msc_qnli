stations_premise = 18
stations_hypothesis = float(input("Enter the number of stations between Hyderabad and Bangalore: "))

# the hypothesis refers to the number of stations between Hyderabad and Bangalore mentioned in the premise
if stations_premise <= stations_hypothesis:
    # check if the estimate of'stations_hypothesis' contradicts the number of stations in the premise
    label = "contradiction"
elif stations_hypothesis!= stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
