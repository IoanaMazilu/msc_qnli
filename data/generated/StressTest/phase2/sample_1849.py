# Premise: less than 6 friends A, B, C went for week end party to McDonald's restaurant and there they measure there weights in some order in 7 rounds.
# Hypothesis: 3 friends A, B, C went for week end party to McDonald's restaurant and there they measure there weights in some order in 7 rounds.
# Golden Label: neutral

friends_premise = 6
friends_hypothesis = 3
rounds_premise = 7
rounds_hypothesis = 7

# the hypothesis refers to the number of friends and rounds of weight measurement mentioned in the premise
if friends_hypothesis >= friends_premise:
    # check if the number of friends in the hypothesis contradicts the estimate of less than 'friends_premise'
    label = "contradiction"
elif rounds_hypothesis != rounds_premise:
    # check if the number of rounds in the hypothesis contradicts the number of rounds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
