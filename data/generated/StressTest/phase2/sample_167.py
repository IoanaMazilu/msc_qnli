# Premise: In how many ways can you seat 7 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Hypothesis: In how many ways can you seat less than 7 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Golden Label: contradiction

people_premise = 7
people_hypothesis = 7

# the hypothesis refers to the number of people mentioned in the premise
if people_hypothesis < people_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, it is an entailment
    label = "entailment"

print(label)

