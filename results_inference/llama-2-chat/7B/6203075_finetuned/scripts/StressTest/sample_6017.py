jane_age_premise = 20
jane_age_hypothesis = 40

# the hypothesis refers to Jane's age when she started baby-sitting, which is also mentioned in the premise
if jane_age_hypothesis!= jane_age_premise:
    # check if Jane's age in the hypothesis contradicts the age in the premise
    label = "contradiction"
else:
    # if the ages in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
