# Premise: Ayesha's father was more than 28 years of age when she was born while her mother was 36 years old when her brother four years younger to her was born.
# Hypothesis: Ayesha's father was 38 years of age when she was born while her mother was 36 years old when her brother four years younger to her was born.
# Golden Label: neutral

father_age_premise = 28
father_age_hypothesis = 38
mother_age_premise = 36
mother_age_hypothesis = 36

# 'father_age_hypothesis' refers to the age of Ayesha's father when she was born, which is also mentioned in the premise
if father_age_hypothesis <= father_age_premise:
    # check if the hypothesis age contradicts the estimate of more than 'father_age_premise' in the premise
    label = "contradiction"
elif mother_age_hypothesis != mother_age_premise:
    # check if the age of the mother in the hypothesis contradicts the age of the mother in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Ayesha's father
    # 'father_age_hypothesis' greater than 'father_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

