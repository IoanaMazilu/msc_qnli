# Premise: In how many ways can you seat 6 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Hypothesis: In how many ways can you seat less than 8 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Golden Label: entailment

people_premise = 6
people_hypothesis = 8

# The hypothesis refers to the number of people that can be seated on a bench mentioned in the premise.
if people_premise >= people_hypothesis:
    # Check if the number of people in the hypothesis contradicts the number of people in the premise.
    label = "contradiction"
elif people_premise < people_hypothesis:
    # If the number of people in the hypothesis is more than the premise, we can infer entailment.
    label = "entailment"

print(label)

