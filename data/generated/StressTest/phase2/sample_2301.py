# Premise: In how many ways can you seat 8 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Hypothesis: In how many ways can you seat more than 6 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Golden Label: entailment

people_seated_premise = 8
people_seated_hypothesis = 6

# the hypothesis refers to the number of people to be seated on a bench, which is also mentioned in the premise
if people_seated_premise <= people_seated_hypothesis:
    # check if the 'people_seated_hypothesis' contradicts the number of people to be seated in the premise
    label = "contradiction"
elif people_seated_hypothesis < people_seated_premise:
    # check if the number of people to be seated in the hypothesis is less than the number of people to be seated in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

