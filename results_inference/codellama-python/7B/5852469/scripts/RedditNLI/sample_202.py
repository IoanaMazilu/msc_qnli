salary_premise = 100000
salary_hypothesis = 100000

# the hypothesis and premise mention the same number
if salary_hypothesis!= salary_premise:
    # check if the number in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # the hypothesis and premise mention the same number
    # any number in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
