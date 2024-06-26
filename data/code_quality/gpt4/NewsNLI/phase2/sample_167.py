pilots_premise = 2
passengers_premise = 3
pilots_hypothesis = 2
passengers_hypothesis = 3

# the hypothesis mentions the number of pilots and passengers who died, which is also referenced in the premise
if pilots_hypothesis != pilots_premise:
    # check if the number of pilots in the hypothesis contradicts the number of pilots mentioned in the premise
    label = "contradiction"
elif passengers_hypothesis != passengers_premise:
    # check if the number of passengers from the hypothesis contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
