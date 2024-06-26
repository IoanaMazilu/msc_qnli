premise_crayons = 479.0
hypothesis_crayons = 345.0

# the hypothesis refers to the number of crayons that were lost or given away
# compute the total number of crayons that were used
total_crayons = premise_crayons - hypothesis_crayons

# check if the number of crayons used contradicts the number of crayons from the premise
if total_crayons!= hypothesis_crayons:
    label = "contradiction"
else:
    label = "entailment"

print(label)
