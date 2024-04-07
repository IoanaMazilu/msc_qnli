# Premise: Sobha's father was more than 28 years of age when she was born while her mother was 36 years old when her brother four years younger to her was born.
# Hypothesis: Sobha's father was 38 years of age when she was born while her mother was 36 years old when her brother four years younger to her was born.
# Golden Label: neutral

father_age_premise = 28
father_age_hypothesis = 38
mother_age_premise = 36
mother_age_hypothesis = 36

# the hypothesis refers to the age of Sobha's parents at the time of her and her brother's birth, which is also mentioned in the premise
if father_age_hypothesis <= father_age_premise:
    # check whether the age of the father at Sobha's birth in the hypothesis contradicts the premise
    label = "contradiction"
elif mother_age_hypothesis != mother_age_premise:
    # check whether the age of the mother at Sobha's brother's birth in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only a lower limit for the age of Sobha's father
    # any age greater than 'father_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

