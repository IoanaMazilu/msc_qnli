seasons_premise = 24
seasons_hypothesis = 24

# the hypothesis talks about the number of seasons Reinsdorf was the chairman of the White Sox, which is also mentioned in the premise
if seasons_hypothesis!= seasons_premise:
    # check if the number of seasons in the hypothesis contradicts the number of seasons in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
