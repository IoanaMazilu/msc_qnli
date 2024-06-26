# the hypothesis is about the same condition for the movie of the year consideration
# compare the condition in the hypothesis with the premise
condition_hypothesis = 1/4
condition_premise = 4/4

if condition_hypothesis >= condition_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
