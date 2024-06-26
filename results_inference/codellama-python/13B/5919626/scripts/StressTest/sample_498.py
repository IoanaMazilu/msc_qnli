shirt_premise = 1
shirt_hypothesis = 1
jeans_premise = 1
jeans_hypothesis = 1
sneakers_premise = 1
sneakers_hypothesis = 1

# the hypothesis talks about the number of shirts, jeans and sneakers in a outfit, referenced also in the premise
if shirt_premise!= shirt_hypothesis or jeans_premise!= jeans_hypothesis or sneakers_premise!= sneakers_hypothesis:
    # check if the hypothesis values and estimates do not contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of outfits
    # any number of outfits is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
