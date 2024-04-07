# Premise: If it takes Darcy a total of 15 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Hypothesis: If it takes Darcy a total of more than 15 more minutes to commute to work by walking than it takes her to commute to work by riding the train, what is the value of x?
# Golden Label: contradiction

commute_diff_premise = 15
commute_diff_hypothesis = 15

# the hypothesis discusses the difference in commute times, referenced also in the premise
if commute_diff_hypothesis != commute_diff_premise:
    # check if the hypothesis value contradicts the exact commute difference in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

