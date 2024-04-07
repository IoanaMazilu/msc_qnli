# Premise: In how many ways can you seat 6 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Hypothesis: In how many ways can you seat 7 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Golden Label: contradiction

people_premise = 6
people_hypothesis = 7

# the hypothesis talks about the number of people that can be seated on a bench, referenced also in the premise
if people_hypothesis != people_premise:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the number of people in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

