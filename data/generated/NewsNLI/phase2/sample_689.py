# Premise: A pioneering study into malaria transmission in Kenya, using data gleaned from the cell phones of nearly 15 million people, has given scientists new clues into how the deadly disease spreads.
# Hypothesis: Researchers use cell phone data to track movement of about 15 million people.
# Golden Label: neutral

people_premise = 15000000
people_hypothesis = 15000000

# the hypothesis mentions the number of people whose cell phone data was used, which is also referenced in the premise
if people_hypothesis == people_premise:
    # if the number of people in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of people in the hypothesis is different from the premise, it would be a contradiction
    label = "contradiction"

print(label)

