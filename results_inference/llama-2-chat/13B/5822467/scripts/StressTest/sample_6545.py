father_age_premise = 38
mother_age_premise = 36
sister_age_premise = 4
brother_age_premise = 4

father_age_hypothesis = 18

# the hypothesis refers to the age of Ayesha's father and mother when she and her brother were born
if father_age_hypothesis >= father_age_premise and mother_age_hypothesis == mother_age_premise:
    # the hypothesis values are consistent with the premise values, so we can infer entailment
    label = "entailment"
elif brother_age_premise!= brother_age_hypothesis:
    # the number of years younger to Ayesha's brother in the hypothesis contradicts the number of years younger to Ayesha's brother in the premise
    label = "contradiction"
else:
    # the premise only gives an estimate for the age of Ayesha's father and mother when she and her brother were born
    # any age values consistent with the premise are consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
