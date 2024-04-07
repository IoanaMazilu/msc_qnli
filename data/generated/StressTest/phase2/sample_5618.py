# Premise: In how many ways can you seat 8 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Hypothesis: In how many ways can you seat 6 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Golden Label: contradiction

people_premise = 8
people_hypothesis = 6

# the hypothesis is about seating people on a bench with Rohit's conditions, as in the premise
if people_hypothesis > people_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif people_hypothesis < people_premise:
    # the premise talks about 8 people while the hypothesis talks about 6
    # the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"
else:
    # if the number of people in the hypothesis equals the number of people in the premise, we can infer entailment
    label = "entailment"

print(label)

