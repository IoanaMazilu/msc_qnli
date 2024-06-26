geese_premise = 58.0
ducks_premise = 37.0
geese_hypothesis = 21.0

# the hypothesis refers to the number of geese, which are also mentioned in the premise
# compute the total number of geese in the premise
total_geese_premise = geese_premise + geese_hypothesis
if total_geese_premise!= geese_premise:
    # check if the number of geese in the hypothesis contradicts the number of geese from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
