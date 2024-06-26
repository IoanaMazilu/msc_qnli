# The premise and hypothesis both refer to the number of different outfits Jordan has
# However, the hypothesis specifies the number of shirts, jeans, and sneakers in each outfit
# We can infer that the number of shirts, jeans, and sneakers in each outfit in the hypothesis is less than 5, which is the same as in the premise
# However, the hypothesis does not entail the number of outfits, as it does not provide a value for the number of outfits
# Therefore, the relation is neutral

outfits_premise = 5
shirts_hypothesis = 1
jeans_hypothesis = 1
sneakers_hypothesis = 1

if outfits_premise > 5:
    # Check if the number of outfits in the hypothesis contradicts the premise
    label = "contradiction"
elif shirts_hypothesis > outfits_premise:
    # Check if the number of shirts in the hypothesis contradicts the premise
    label = "contradiction"
elif jeans_hypothesis > outfits_premise:
    # Check if the number of jeans in the hypothesis contradicts the premise
    label = "contradiction"
elif sneakers_hypothesis > outfits_premise:
    # Check if the number of sneakers in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, the relation is neutral
    label = "neutral"

print(label)
