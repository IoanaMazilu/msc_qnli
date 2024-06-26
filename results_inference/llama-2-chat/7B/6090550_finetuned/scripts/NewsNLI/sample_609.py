women_ceos_premise = 500
women_ceos_hypothesis = 18

# the hypothesis mentions the number of women CEOs, which is also mentioned in the premise
# however, the hypothesis provides a specific number for women CEOs, while the premise gives only a range
# we need to compare the specific number in the hypothesis with the range given in the premise
if women_ceos_hypothesis >= women_ceos_premise:
    # if the specific number in the hypothesis is greater than or equal to the range in the premise, we can infer entailment
    label = "entailment"
else:
    # if the specific number in the hypothesis is less than the range in the premise, we can infer contradiction
    label = "contradiction"

print(label)
