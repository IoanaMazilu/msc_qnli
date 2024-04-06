# Premise: U.S. Already $292 Billion in the Red This Year.
# Hypothesis: U.S. already $292 bln in the red this year-CBO.
# Golden Label: entailment

debt_premise = 292 * 10**9  # converting Billion to actual number
debt_hypothesis = 292 * 10**9  # converting bln to actual number

# Both the premise and hypothesis mention the same debt amount for the US this year
if debt_premise != debt_hypothesis:
    # check if the debt amount in the hypothesis contradicts the debt amount in the premise
    label = "contradiction"
else:
    # if the debt amount in the hypothesis does not contradict the debt amount in the premise, we can infer entailment
    label = "entailment"

print(label)

