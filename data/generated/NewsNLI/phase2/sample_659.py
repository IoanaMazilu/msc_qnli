# Premise: Manning has asked for Lind, instead of the military equivalent of a jury, to decide his guilt or innocence on the 12 charges to which he pleaded not guilty.
# Hypothesis: He has pleaded guilty to 10 of 22 charges against him.
# Golden Label: neutral

charges_premise = 12
charges_hypothesis = 10

# the hypothesis mentions the number of charges to which Manning pleaded guilty, which is also referenced in the premise
# but, the premise and hypothesis state different numbers of charges
if charges_hypothesis != charges_premise:
    # check if the number of charges from the hypothesis contradicts the number of charges in the premise
    label = "contradiction"

print(label)

