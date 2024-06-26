father_age_premise = 2 * shankar_age_premise + 10
father_age_hypothesis = 2 * shankar_age_hypothesis + 80

# the hypothesis refers to the age of Ayisha's father and Shankar mentioned in the premise
if father_age_premise > father_age_hypothesis:
    # check if the age of Ayisha's father in the premise contradicts the hypothesis
    label = "contradiction"
elif father_age_premise < father_age_hypothesis:
    # if the age of Ayisha's father in the premise is less than the age in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the age of Ayisha's father in the premise is equal to the age in the hypothesis, we can infer neutrality
    label = "neutral"

print(label)
