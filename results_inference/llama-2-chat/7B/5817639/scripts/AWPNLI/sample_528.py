girls_premise = 542.0
boys_premise = 387.0
girls_hypothesis = 155.0

# compare the number of girls and boys in the premise
if girls_hypothesis > girls_premise:
    label = "entailment"
elif girls_hypothesis < girls_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
