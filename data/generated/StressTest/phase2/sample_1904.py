# Premise: There are 24 stations between Ernakulam and Chennai.
# Hypothesis: There are 44 stations between Ernakulam and Chennai.
# Golden Label: contradiction

stations_premise = 24
stations_hypothesis = 44

# the hypothesis refers to the number of stations between Ernakulam and Chennai, mentioned also in the premise
if stations_hypothesis != stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
