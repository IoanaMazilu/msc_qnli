# Premise: The ratio of men to women in the Snyder community choir is 6 to 5.
# Hypothesis: The ratio of men to women in the Snyder community choir is more than 3 to 5.
# Golden Label: entailment

men_women_ratio_premise = 6 / 5
men_women_ratio_hypothesis = 3 / 5

# the hypothesis refers to the ratio of men to women in the choir, mentioned also in the premise
if men_women_ratio_premise <= men_women_ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

