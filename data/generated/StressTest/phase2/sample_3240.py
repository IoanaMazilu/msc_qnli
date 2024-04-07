# Premise: There are 18 stations between Hyderabad and Bangalore.
# Hypothesis: There are less than 38 stations between Hyderabad and Bangalore.
# Golden Label: entailment

stations_premise = 18
stations_hypothesis = 38

# the hypothesis refers to the number of stations between two cities mentioned in the premise
if stations_premise >= stations_hypothesis:
    # check if the estimate of 'stations_premise' contradicts the number of stations in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

