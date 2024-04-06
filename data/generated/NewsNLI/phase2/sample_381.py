# Premise: Around 80 people have been wounded in the push, the military said.
# Hypothesis: Around 80 people have been wounded, Turkish military says.
# Golden Label: entailment

wounded_people_premise = 80
wounded_people_hypothesis = 80

# the hypothesis mentions the number of people that have been wounded, which is also mentioned in the premise
# however, the hypothesis specifies that this information is from the Turkish military, which cannot be entailed from the premise
label = "neutral"

print(label)

