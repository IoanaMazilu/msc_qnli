# Premise: Ayesha's father was less than 50 years of age when she was born while her mother was 22 years old when her brother four years younger to her was born.
# Hypothesis: Ayesha's father was 30 years of age when she was born while her mother was 22 years old when her brother four years younger to her was born.
# Golden Label: neutral

father_age_premise = 50
father_age_hypothesis = 30
mother_age_premise = 22
mother_age_hypothesis = 22

# the hypothesis refers to the age of Ayesha's parents at the time of her and her brother's birth, mentioned in the premise
if father_age_hypothesis >= father_age_premise:
    # check if the age of Ayesha's father at her birth in the hypothesis contradicts the age in the premise
    label = "contradiction"
elif mother_age_hypothesis != mother_age_premise:
    # check if the age of Ayesha's mother at her brother's birth in the hypothesis contradicts the age in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, and the hypothesis does not give more precise estimates than the premise, we can infer entailment
    label = "entailment"

print(label)

