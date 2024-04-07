# Premise: Present ages of Sameer and Anand are in the ratio of 5:4 respectively.
# Hypothesis: Present ages of Sameer and Anand are in the ratio of more than 1:4 respectively.
# Golden Label: entailment

sameer_anand_ratio_premise = 5/4
sameer_anand_ratio_hypothesis = 1/4

# the hypothesis talks about the ratio of Sameer and Anand's ages, which is also mentioned in the premise
if sameer_anand_ratio_premise <= sameer_anand_ratio_hypothesis:
    # check if the ratio of 'sameer_anand_ratio_hypothesis' contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # the premise gives a specific ratio for the ages
    # any ratio greater than 'sameer_anand_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

