jhon_works_premise = 60
jhon_works_hypothesis = 30

# the hypothesis refers to the number of days Jhon works, mentioned in the premise
if jhon_works_premise > jhon_works_hypothesis:
    # check if the hypothesis value contradicts the number of days Jhon works in the premise
    label = "contradiction"
elif jhon_works_hypothesis == 0:
    # check if the hypothesis value is neutral, as it does not provide any information about the number of days Jhon works
    label = "neutral"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
