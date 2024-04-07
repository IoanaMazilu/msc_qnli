# Premise: Jane started baby-sitting when she was 20 years old.
# Hypothesis: Jane started baby-sitting when she was less than 40 years old.
# Golden Label: entailment

start_age_premise = 20
start_age_hypothesis = 40

# the hypothesis refers to the age when Jane started babysitting, which is also mentioned in the premise
if start_age_hypothesis < start_age_premise:
    # check if the age in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
elif start_age_hypothesis == start_age_premise:
    # if the hypothesis age is exactly the same as in the premise, we have entailment
    label = "entailment"
else:
    # any age higher than 'start_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

