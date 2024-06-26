months_later_premise = 4
months_later_hypothesis = 2

# the hypothesis talks about the time Jose joined, also mentioned in the premise
if months_later_hypothesis >= months_later_premise:
    # check if the hypothesis value contradicts the estimate of less than 'months_later_premise'
    label = "contradiction"
elif months_later_hypothesis < months_later_premise:
    # if the number of months in the hypothesis is less than the number in the premise, we can infer entailment
    label = "entailment"

print(label)
