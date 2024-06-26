months_premise = 6
months_hypothesis = 2

# the hypothesis refers to the number of months that Jose joined him later, which is also mentioned in the premise
if months_hypothesis >= months_premise:
    # check if the hypothesis value contradicts the estimate of less than 'months_premise'
    label = "contradiction"
elif months_hypothesis < months_premise:
    # if the number of months in the hypothesis is less than the premise, we can infer entailment
    label = "entailment"

print(label)
