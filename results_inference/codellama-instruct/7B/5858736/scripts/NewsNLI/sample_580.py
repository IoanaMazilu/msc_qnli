trucks_premise = 80
trucks_hypothesis = 3

if trucks_hypothesis!= trucks_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
