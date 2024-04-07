# Premise: Ayesha's father was 30 years of age when she was born while her mother was 22 years old when her brother four years younger to her was born.
# Hypothesis: Ayesha's father was 80 years of age when she was born while her mother was 22 years old when her brother four years younger to her was born.
# Golden Label: contradiction

father_age_premise = 30
father_age_hypothesis = 80
mother_age_premise = 22
mother_age_hypothesis = 22

# the hypothesis refers to the ages of Ayesha's parents when she and her brother were born
if father_age_premise != father_age_hypothesis:
    # check if the father's age at Ayesha's birth in the hypothesis contradicts the father's age reported in the premise
    label = "contradiction"
elif mother_age_premise != mother_age_hypothesis:
    # check if the mother's age at the brother's birth in the hypothesis contradicts the mother's age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

