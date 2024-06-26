years_old_premise = 32
years_old_hypothesis = 42
years_since_stopped_babysitting_premise = 10
years_since_stopped_babysitting_hypothesis = 10

# the hypothesis talks about the age and years since stopping baby-sitting of Jane, referenced also in the premise
if years_old_hypothesis <= years_old_premise:
    # check if the hypothesis value contradicts the age of Jane in the premise
    label = "contradiction"
elif years_since_stopped_babysitting_hypothesis!= years_since_stopped_babysitting_premise:
    # check if the number of years since stopping baby-sitting in the hypothesis contradicts the number of years since stopping baby-sitting reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Jane
    # any age greater than 'years_old_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
