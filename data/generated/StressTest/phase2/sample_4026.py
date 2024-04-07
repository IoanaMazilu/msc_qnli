# Premise: Richard will arrange 6 people of 6 different heights for photograph by placing them in two rows of three so that each person in the first row is standing is standing in front of someone in the second row.
# Hypothesis: Richard will arrange less than 7 people of 6 different heights for photograph by placing them in two rows of three so that each person in the first row is standing is standing in front of someone in the second row.
# Golden Label: entailment

people_premise = 6
people_hypothesis = 7

# the hypothesis refers to the number of people Richard will arrange, mentioned in the premise
if people_hypothesis <= people_premise:
    # check if the estimate of 'people_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
