seasons_premise = 24
championships_premise = 3
championship_year_premise = 2000
championships_hypothesis = 24

# the hypothesis talks about the total number of championships the White Sox have won, which is also mentioned in the premise
if championships_hypothesis!= championships_premise:
    # check if the total number of championships in the hypothesis contradicts the number of championships from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
