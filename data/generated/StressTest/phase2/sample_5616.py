# Premise: In how many ways can you seat 8 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Hypothesis: In how many ways can you seat more than 1 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Golden Label: entailment

people_premise = 8
people_hypothesis = 1

# the hypothesis refers to the seating arrangement of people, mentioned also in the premise
if people_hypothesis >= people_premise:
    # check if the hypothesis contradicts the number of people mentioned in the premise
    label = "contradiction"
elif people_hypothesis != people_premise - 1:
    # the premise gives the exact number of people
    # any number of people other than 'people_premise - 1' cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

