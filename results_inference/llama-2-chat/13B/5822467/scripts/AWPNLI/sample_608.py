geese_premise = 58.0
ducks_premise = 37.0
total_birds_premise = geese_premise + ducks_premise
hypothesis_geese = 21.0

# compare the total number of birds in the premise and the hypothesis
if total_birds_premise!= hypothesis_geese + geese_premise:
    # check if the number of geese in the hypothesis contradicts the number of birds in the premise
    label = "contradiction"
elif ducks_premise!= hypothesis_geese:
    # check if the number of ducks in the hypothesis contradicts the number of ducks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
