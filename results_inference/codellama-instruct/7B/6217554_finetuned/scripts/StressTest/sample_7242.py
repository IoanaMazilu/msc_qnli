father_age_premise = 10
father_age_hypothesis = 80

# the hypothesis talks about the time after which Ayisha's father's age will be twice Shankar's age
# any time greater than 'father_age_premise' contradicts the premise
if father_age_hypothesis <= father_age_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time greater than 'father_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
