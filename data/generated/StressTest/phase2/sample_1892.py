# Premise: There are 10 stations between Trichy and Chennai.
# Hypothesis: There are 50 stations between Trichy and Chennai.
# Golden Label: contradiction

stations_premise = 10
stations_hypothesis = 50

# the hypothesis refers to the number of stations between two cities, also mentioned in the premise
if stations_hypothesis != stations_premise:
    # check if the exact number of stations in the hypothesis contradicts the exact number of stations mentioned in the premise
    label = "contradiction"
else:
    # if the number of stations in the hypothesis is the same as in the premise, we have an entailment
    label = "entailment"

print(label)

