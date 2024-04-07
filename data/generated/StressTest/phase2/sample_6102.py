# Premise: Jane started baby-sitting when she was 18 years old.
# Hypothesis: Jane started baby-sitting when she was less than 78 years old.
# Golden Label: entailment

start_age_premise = 18
start_age_hypothesis = 78

# the hypothesis refers to the age Jane started babysitting, also mentioned in the premise
if start_age_hypothesis < start_age_premise:
    # check if the hypothesis age contradicts the age in the premise
    label = "contradiction"
elif start_age_hypothesis == start_age_premise:
    # check if the hypothesis age equals the age in the premise
    label = "entailment"
else:
    # if the hypothesis age does not contradict the premise age and is not equal to it, we infer neutral
    label = "neutral"

print(label)

