stations_premise = 8
stations_hypothesis = 2

# the hypothesis talks about the number of stations between two cities, referenced also in the premise
if stations_hypothesis > stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations in the premise
    label = "contradiction"
elif stations_hypothesis == stations_premise:
    # if the number of stations in the hypothesis is equal to the number of stations in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis number of stations is less than the premise number of stations, we cannot infer entailment
    label = "neutral"

print(label)
