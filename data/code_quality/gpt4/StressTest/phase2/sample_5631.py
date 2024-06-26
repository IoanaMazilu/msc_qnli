mary_age_diff_premise = 22
mary_age_diff_hypothesis = 42

# the hypothesis refers to the age difference between Mary and Albert mentioned in the premise
if mary_age_diff_premise > mary_age_diff_hypothesis:
    # check if the age difference in the premise contradicts the 'less than' age difference in the hypothesis
    label = "contradiction"
elif mary_age_diff_premise < mary_age_diff_hypothesis:
    # if the age difference in the premise is less than the age difference in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the age difference in the premise is equal to the age difference in the hypothesis, it's still consistent with 'less than'
    label = "entailment"

print(label)
