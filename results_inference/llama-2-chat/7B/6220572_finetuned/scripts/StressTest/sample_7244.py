father_age_premise = 0
father_age_hypothesis = 0

# the hypothesis talks about the future age of Ayisha's father, referenced also in the premise
if father_age_hypothesis!= father_age_premise + 30:
    # check if the future age in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the future age
    # any future age greater than 'father_age_premise + 30' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
