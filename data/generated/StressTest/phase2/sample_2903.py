# Premise: 6 friends go out to dinner at Outback Steakhouse.
# Hypothesis: 7 friends go out to dinner at Outback Steakhouse.
# Golden Label: contradiction

friends_premise = 6
friends_hypothesis = 7

# the hypothesis talks about the number of friends going out to dinner at Outback Steakhouse, referenced also in the premise
if friends_hypothesis != friends_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends reported in the premise
    label = "contradiction"
else:
    # if the number of friends in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

