# Premise: Akash will arrange 6 people of 6 different heights for photograph by placing them in two rows of three so that each person in the first row is standing is standing in front of someone in the second row.
# Hypothesis: Akash will arrange less than 8 people of 6 different heights for photograph by placing them in two rows of three so that each person in the first row is standing is standing in front of someone in the second row.
# Golden Label: entailment

people_premise = 6
people_hypothesis = 8

# the hypothesis refers to the number of people Akash will arrange for photograph mentioned in the premise
if people_premise >= people_hypothesis:
    # check if the number of 'people_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the number of people in the hypothesis is less than the number of people in the premise, we can infer entailment
    label = "entailment"

print(label)

