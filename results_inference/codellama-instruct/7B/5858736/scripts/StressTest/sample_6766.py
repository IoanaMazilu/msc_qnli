people_bcc_premise = 63
people_bcc_hypothesis = 13

if people_bcc_hypothesis >= people_bcc_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
