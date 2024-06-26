box_crayons_premise = 479.0
left_crayons_premise = 134.0
lost_crayons_hypothesis = 345.0

# compute the difference between the number of crayons in the premise and the number of crayons lost in the hypothesis
diff = lost_crayons_hypothesis - left_crayons_premise

# if the difference is negative, it means the hypothesis contradicts the premise
if diff < 0:
    label = "contradiction"
elif lost_crayons_hypothesis == left_crayons_premise:
    # if the number of lost crayons in the hypothesis is equal to the number of left crayons in the premise,
    # then there is no contradiction or entailment, just neutrality
    label = "neutral"
else:
    # if the number of lost crayons in the hypothesis is greater than the number of left crayons in the premise,
    # then the hypothesis entails the premise
    label = "entailment"

print(label)
