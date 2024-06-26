baking_soda_premise = 8
baking_soda_hypothesis = 2

# the hypothesis talks about the quantity of baking soda in Bob's pizza recipe, referenced also in the premise
if baking_soda_hypothesis >= baking_soda_premise:
    # check if the hypothesis value contradicts the estimate of less than 'baking_soda_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of baking soda
    # any quantity of baking soda less than 'baking_soda_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
