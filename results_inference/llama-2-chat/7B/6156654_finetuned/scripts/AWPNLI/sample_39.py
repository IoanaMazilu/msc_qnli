crayons_premise = 7.0
crayons_taken_premise = 3.0
crayons_hypothesis = 0.0

# the hypothesis refers to the number of crayons left in the drawer, which is also mentioned in the premise
# the premise gives the exact number of crayons left and the number of crayons taken
# the hypothesis contradicts the premise by stating that there are no crayons left, which is not the case

if crayons_hypothesis == crayons_premise:
    # check if the hypothesis value and the premise value are the same
    label = "entailment"
else:
    # if the hypothesis value and the premise value are different, it's a contradiction
    label = "contradiction"

print(label)
