stations_delhi_chennai_premise = 85
stations_delhi_chennai_hypothesis = 25

if stations_delhi_chennai_hypothesis >= stations_delhi_chennai_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
