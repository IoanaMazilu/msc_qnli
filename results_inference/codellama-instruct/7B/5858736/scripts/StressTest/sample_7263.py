women_men_premise = 4
women_men_hypothesis = 6

if women_men_hypothesis >= women_men_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
