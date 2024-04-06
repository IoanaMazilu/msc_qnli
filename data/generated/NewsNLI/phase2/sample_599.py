# Premise: Two women and their two dogs were rescued after flood waters trapped them inside a house in the rural community of New River north of Phoenix, according to Amanda Jacinto, spokeswoman for the fire department in the Phoenix suburb of Peoria.
# Hypothesis: Two women were trapped inside a house as waters smashed into its foundation.
# Golden Label: neutral

women_rescued_premise = 2
dogs_rescued_premise = 2
women_trapped_hypothesis = 2

# the hypothesis mentions the number of women trapped inside a house, which is also referenced in the premise
# however, the hypothesis does not mention the dogs that were also trapped and rescued, as stated in the premise
if women_trapped_hypothesis != women_rescued_premise:
    # check if the number of women in the hypothesis contradicts the number of women rescued in the premise
    label = "contradiction"
else:
    # if the number of women in the hypothesis does not contradict the number of women rescued in the premise,
    # but the premise contains more information (about the dogs), we can infer neutrality
    label = "neutral"

print(label)
