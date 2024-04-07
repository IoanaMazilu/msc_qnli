# Premise: Jane and Thomas are among the 7 people from which a committee of 3 people is to be selected.
# Hypothesis: Jane and Thomas are among the 5 people from which a committee of 3 people is to be selected.
# Golden Label: contradiction

people_premise = 7
people_hypothesis = 5

# the hypothesis refers to the number of people from which a committee is selected, a number also mentioned in the premise
if people_premise < people_hypothesis:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis number does not contradict the premise number, we can infer entailment
    label = "entailment"

print(label)
