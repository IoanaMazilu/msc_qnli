keith_pears = 47.0
mike_pears = 12.0
keith_gave_pears = 46.0

# the hypothesis refers to the number of pears left for Mike, which can be calculated from the premise
mike_left_pears = keith_pears - keith_gave_pears - mike_pears

if mike_left_pears!= 13.0:
    # check if the calculated number of pears left for Mike contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and calculations match, we can infer entailment
    label = "entailment"

print(label)
