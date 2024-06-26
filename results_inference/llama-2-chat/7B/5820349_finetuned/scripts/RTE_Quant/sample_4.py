seasons_premise = 24
championships_hypothesis = 24

# the hypothesis talks about the number of championships won by the White Sox, which is also mentioned in the premise
if championships_hypothesis!= seasons_premise:
    # check if the number of championships in the hypothesis contradicts the number of seasons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
