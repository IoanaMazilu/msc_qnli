people_entered_premise = 15
people_entered_hypothesis = 15

# the hypothesis mentions the number of people who entered the theater before Sujit
# the premise gives the number of people who entered the theater before Sujit
if people_entered_hypothesis == people_entered_premise:
    label = "entailment"
elif people_entered_hypothesis < people_entered_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
