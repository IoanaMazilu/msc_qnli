# Premise: In how many ways can you seat 5 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Hypothesis: In how many ways can you seat more than 5 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Golden Label: contradiction

people_seating_premise = 5
people_seating_hypothesis = 5

# The hypothesis talks about the number of people being seated on a bench, a number also mentioned in the premise.
if people_seating_hypothesis > people_seating_premise:
    # If the number in the hypothesis is greater than the number in the premise, it contradicts the premise.
    label = "contradiction"
elif people_seating_hypothesis < people_seating_premise:
    # If the number in the hypothesis is less than the number in the premise, it contradicts the premise.
    label = "contradiction"
else:
    # If the number in the hypothesis is equal to the number in the premise, it entails the premise.
    label = "entailment"

print(label)

