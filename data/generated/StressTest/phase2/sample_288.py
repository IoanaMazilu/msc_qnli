# Premise: Jane and Thomas are among the 7 people from which a committee of 3 people is to be selected.
# Hypothesis: Jane and Thomas are among the more than 1 people from which a committee of 3 people is to be selected.
# Golden Label: entailment

people_premise = 7
people_hypothesis = 1
committee_size = 3

# the hypothesis refers to the people (Jane and Thomas) and committees mentioned in the premise
if people_hypothesis >= people_premise:
    # check if the people_hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

