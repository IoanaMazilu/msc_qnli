# Premise: In how many ways can you seat 4 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Hypothesis: In how many ways can you seat less than 7 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Golden Label: entailment

people_premise = 4
people_hypothesis = 7

# the hypothesis talks about the number of people that can be seated on a bench, referenced also in the premise
if people_hypothesis <= people_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives a specific number for the people
    # any number of people greater than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

