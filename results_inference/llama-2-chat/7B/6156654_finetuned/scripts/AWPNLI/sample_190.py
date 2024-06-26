crayons_premise = 479.0
crayons_left_premise = 134.0
crayons_lost_hypothesis = 345.0

# the hypothesis refers to the number of crayons lost or given away, which is also mentioned in the premise
# compute the number of crayons left after the lost ones were given away according to the hypothesis
crayons_left_after_lost = crayons_left_premise - crayons_lost_hypothesis

# check if the number of crayons left after the lost ones were given away contradicts the number of crayons left in the premise
if crayons_left_after_lost!= crayons_left_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
