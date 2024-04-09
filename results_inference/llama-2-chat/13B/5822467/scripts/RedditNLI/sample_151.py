import_drop_premise = -2.2
brent_drop_hypothesis = -2.5

# the premise and hypothesis mention the drop in import prices and Brent crude prices, respectively
if import_drop_premise!= brent_drop_hypothesis:
    # check if the drop in Brent crude prices contradicts the drop in import prices in the premise
    label = "contradiction"
elif brent_drop_hypothesis < import_drop_premise:
    # check if the drop in Brent crude prices is less than the drop in import prices in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the drop in import prices
    # any estimate of the drop in Brent crude prices greater or equal to the drop in import prices in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
