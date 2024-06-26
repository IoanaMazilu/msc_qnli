artwork_stolen_premise = 5
artwork_stolen_hypothesis = 5

# the hypothesis talks about the percentage of stolen artworks that are returned to the owners, which is also mentioned in the premise
if artwork_stolen_hypothesis!= artwork_stolen_premise:
    # check if the percentage of stolen artworks returned in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
