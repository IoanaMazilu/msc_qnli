total_pens_premise = 10
total_pens_hypothesis = 10

# the hypothesis refers to the total number of pens Elena purchased, as given in the premise
if total_pens_hypothesis < total_pens_premise:
    # check if the hypothesis value contradicts the total number of pens purchased according to the premise
    label = "contradiction"
elif total_pens_hypothesis == total_pens_premise:
    # if the total number of pens in the hypothesis equals the number in the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives only a specific number for the total pens
    # any number of pens greater than 'total_pens_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
