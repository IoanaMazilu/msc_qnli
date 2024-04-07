# Premise: There are 15 stations between Hyderabad and Bangalore.
# Hypothesis: There are 75 stations between Hyderabad and Bangalore.
# Golden Label: contradiction

stations_premise = 15
stations_hypothesis = 75

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, referenced also in the premise
if stations_hypothesis != stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

