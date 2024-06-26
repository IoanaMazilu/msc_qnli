geese_premise = 58.0
ducks_premise = 37.0
more_geese_hypothesis = 21.0

# the hypothesis talks about the number of geese and ducks, which are also referenced in the premise
# compute the total number of geese and ducks in the premise
total_geese_premise = geese_premise
total_ducks_premise = ducks_premise

# check if the number of geese from the hypothesis contradicts the number of geese in the premise
if more_geese_hypothesis!= total_geese_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
