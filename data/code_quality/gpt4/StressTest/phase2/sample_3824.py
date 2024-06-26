stations_premise = 16
stations_hypothesis = 36

# the hypothesis talks about the number of stations between Mumbai and Chennai, referenced also in the premise
if stations_hypothesis == stations_premise:
    # check if the number of stations in the hypothesis matches the number of stations in the premise
    label = "entailment"
elif stations_hypothesis != stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "contradiction"

print(label)
