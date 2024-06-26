charges_premise = 12
charges_hypothesis = 10

# the hypothesis mentions the number of charges to which Manning pleaded guilty, which is also referenced in the premise
# but, the premise and hypothesis state different numbers of charges
if charges_hypothesis != charges_premise:
    # check if the number of charges from the hypothesis contradicts the number of charges in the premise
    label = "contradiction"

print(label)
