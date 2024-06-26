stolen_art_premise = 0.05
stolen_art_hypothesis = 0.05

# the hypothesis talks about the percentage of stolen art that gets returned to the owners, which is also mentioned in the premise
if stolen_art_hypothesis!= stolen_art_premise:
    # check if the percentage of stolen art in the hypothesis contradicts the percentage from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
