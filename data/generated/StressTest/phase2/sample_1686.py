# Premise: There are 17 stations between Hyderabad and Bangalore.
# Hypothesis: There are less than 77 stations between Hyderabad and Bangalore.
# Golden Label: entailment

stations_premise = 17
stations_hypothesis = 77

# the hypothesis refers to the number of stations between Hyderabad and Bangalore mentioned in the premise
if stations_hypothesis <= stations_premise:
    # check if the estimate of 'stations_hypothesis' contradicts the number of stations in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

