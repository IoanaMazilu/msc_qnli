# Premise: The ratio of the ages of Mona and Sona is 4:5.
# Hypothesis: The ratio of the ages of Mona and Sona is less than 4:5.
# Golden Label: contradiction

ratio_ages_premise = 4/5
ratio_ages_hypothesis = 4/5

# the hypothesis refers to the ratio of ages of Mona and Sona mentioned in the premise
if ratio_ages_hypothesis < ratio_ages_premise:
    # check if the ratio of ages in the hypothesis is less than the ratio of ages in the premise
    label = "contradiction"
elif ratio_ages_hypothesis > ratio_ages_premise:
    # check if the ratio of ages in the hypothesis is greater than the ratio of ages in the premise
    label = "contradiction"
else:
    # if the ratio of ages in the hypothesis equals the ratio of ages in the premise, it is entailed
    label = "entailment"

print(label)

