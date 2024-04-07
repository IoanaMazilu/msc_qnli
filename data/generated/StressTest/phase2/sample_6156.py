# Premise: Present ages of Sameer and Anand are in the ratio of 5:4 respectively.
# Hypothesis: Present ages of Sameer and Anand are in the ratio of more than 3:4 respectively.
# Golden Label: entailment

# define the premise ratios
sameer_age_ratio_premise = 5
anand_age_ratio_premise = 4

# define the hypothesis ratios
sameer_age_ratio_hypothesis = 3
anand_age_ratio_hypothesis = 4

# the hypothesis refers to the age ratios of Sameer and Anand mentioned in the premise
if sameer_age_ratio_premise <= sameer_age_ratio_hypothesis and anand_age_ratio_premise == anand_age_ratio_hypothesis:
    # check if the ratio of 'sameer_age_ratio_hypothesis' contradicts the Sameer's age ratio in the premise
    label = "contradiction"
elif sameer_age_ratio_premise > sameer_age_ratio_hypothesis and anand_age_ratio_premise == anand_age_ratio_hypothesis:
    # if the Sameer's age ratio in the hypothesis is lower than in the premise and Anand's age ratio is equal in both cases, we can infer entailment
    label = "entailment"
else:
    # if none of the above conditions is met, it means the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise either
    label = "neutral"

print(label)

