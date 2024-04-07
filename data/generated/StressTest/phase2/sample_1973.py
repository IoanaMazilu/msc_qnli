# Premise: There are 18 stations between Hyderabad and Bangalore.
# Hypothesis: There are 28 stations between Hyderabad and Bangalore.
# Golden Label: contradiction

stations_premise = 18
stations_hypothesis = 28

# the hypothesis refers to the number of stations between Hyderabad and Bangalore mentioned in the premise
if stations_hypothesis != stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

