obama_premise = 1
mccain_premise = 1

# the hypothesis mentions Barack Obama and John McCain, which are also mentioned in the premise
if obama_hypothesis == obama_premise and mccain_hypothesis == mccain_premise:
    # if the values of the hypothesis variables match the values of the premise variables, we can infer entailment
    label = "entailment"
else:
    # if the values of the hypothesis variables do not match the values of the premise variables, we can infer contradiction or neutrality
    if obama_hypothesis!= obama_premise or mccain_hypothesis!= mccain_premise:
        label = "contradiction"
    else:
        label = "neutral"

print(label)
