john_age_factor_premise = 3
john_age_factor_hypothesis = 1

# the hypothesis refers to the age relation between John and Mark mentioned in the premise
if john_age_factor_premise <= john_age_factor_hypothesis:
    # check if the 'john_age_factor_hypothesis' contradicts the age relation in the premise
    label = "contradiction"
else:
    # if the age relation factor in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
