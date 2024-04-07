# Premise: Jane started baby-sitting when she was 18 years old.
# Hypothesis: Jane started baby-sitting when she was less than 18 years old.
# Golden Label: contradiction

jane_age_premise = 18
jane_age_hypothesis = 18

# the hypothesis refers to Jane's age when she started babysitting, which is also mentioned in the premise
if jane_age_hypothesis < jane_age_premise:
    # check if the hypothesis value contradicts the exact age mentioned in the premise
    label = "contradiction"
elif jane_age_hypothesis > jane_age_premise:
    # check if the hypothesis value contradicts the exact age mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

