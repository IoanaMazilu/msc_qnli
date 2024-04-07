# Premise: There are 43 stations between Ernakulam and Chennai.
# Hypothesis: There are 73 stations between Ernakulam and Chennai.
# Golden Label: contradiction

stations_premise = 43
stations_hypothesis = 73

# the hypothesis talks about the number of stations between Ernakulam and Chennai, referenced also in the premise
if stations_hypothesis != stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "contradiction"
else:
    # if the number of stations in the hypothesis matches the number of stations in the premise, we can infer entailment
    label = "entailment"

print(label)

