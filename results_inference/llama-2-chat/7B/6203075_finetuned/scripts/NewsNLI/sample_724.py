# the premise and hypothesis both mention the World Cup, Argentina, and South Korea's qualification

# the premise states that Argentina won 2-0 against Greece, and South Korea drew 2-2 with Nigeria
# the hypothesis states that South Korea qualified as runners-up after drawing 2-2 with Nigeria

# we need to compare the information about the South Korea-Nigeria match in the premise and hypothesis
if (Argentina_score_premise!= South_Korea_score_hypothesis) or (South_Korea_score_premise == South_Korea_score_hypothesis):
    # check if the scores of the Argentina and South Korea matches in the premise and hypothesis contradict each other
    label = "contradiction"
else:
    # if the scores do not contradict, we can infer entailment
    label = "entailment"

print(label)
