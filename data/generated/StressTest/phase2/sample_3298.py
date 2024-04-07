# Premise: Albert father was less than 58 years of age when she was born while her mother was 46 years old when her brother 2 years younger to her was born.
# Hypothesis: Albert father was 48 years of age when she was born while her mother was 46 years old when her brother 2 years younger to her was born.
# Golden Label: neutral

father_age_premise = 58
father_age_hypothesis = 48
mother_age_premise = 46
mother_age_hypothesis = 46

# the hypothesis refers to the ages of Albert's parents when she and her brother were born, as mentioned in the premise
if father_age_hypothesis > father_age_premise:
    # check if the age of Albert's father at her birth in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
elif mother_age_hypothesis != mother_age_premise:
    # check if the age of Albert's mother at her brother's birth in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

