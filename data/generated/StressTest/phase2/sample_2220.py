# Premise: There are 17 stations between Hyderabad and Bangalore.
# Hypothesis: There are less than 47 stations between Hyderabad and Bangalore.
# Golden Label: entailment

stations_premise = 17
stations_hypothesis = 47

# the hypothesis refers to the number of stations between Hyderabad and Bangalore mentioned in the premise
if stations_premise >= stations_hypothesis:
    # check if the number of stations in the premise contradicts the estimate of less than 'stations_hypothesis'
    label = "contradiction"
elif stations_hypothesis != stations_premise:
    # check if the number of stations in the hypothesis is the same as in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

