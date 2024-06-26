stations_premise = 18
stations_hypothesis = 78

# the hypothesis talks about the number of stations between two cities, referenced also in the premise
if stations_hypothesis < stations_premise:
    # check if the hypothesis value contradicts the given number of 'stations_premise'
    label = "contradiction"
elif stations_premise != stations_hypothesis:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
