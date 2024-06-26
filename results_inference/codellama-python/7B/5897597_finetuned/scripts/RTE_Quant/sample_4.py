seasons_premise = 24
championships_premise = 3
central_championship_premise = 1

championships_hypothesis = 24

# the hypothesis talks about the number of championships the White Sox have won, which is also mentioned in the premise
if championships_hypothesis!= championships_premise:
    # check if the number of championships in the hypothesis contradicts the number of championships from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
