# Premise: In how many ways can you seat 8 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Hypothesis: In how many ways can you seat less than 8 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Golden Label: contradiction

people_premise = 8
people_hypothesis = 8

# the hypothesis refers to the same seating problem for Rohit mentioned in the premise
if people_hypothesis >= people_premise:
    # check if the hypothesis number of people contradicts the premise's explicit number of people
    label = "contradiction"
else:
    # the premise gives an explicit number of people
    # any number of people less than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

