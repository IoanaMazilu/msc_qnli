raj_age_premise = 30
raj_age_hypothesis = 20

# the hypothesis talks about the comparison of Raj's age to Hema's at a certain age
if raj_age_hypothesis >= raj_age_premise:
    # check if the raj's age in the hypothesis contradicts the estimate of less than 'raj_age_premise'
    label = "contradiction"
elif raj_age_hypothesis == raj_age_premise - 10:
    # check if raj's age in the hypothesis is 10 years less than the raj's age in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the raj's age
    # any age of raj less than 'raj_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
