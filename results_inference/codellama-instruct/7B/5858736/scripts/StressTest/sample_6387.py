balls_given_premise = 100
balls_given_hypothesis = 300

if balls_given_hypothesis >= balls_given_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
