# Premise: Twenty ticket holders will win $1 million after matching all the numbers except the Mega ball.
# Hypothesis: 20 people will win $1 million after matching the five non-Mega ball numbers.
# Golden Label: entailment

winners_premise = 20
winners_hypothesis = 20
prize_premise = 1000000
prize_hypothesis = 1000000

# the hypothesis mentions the number of winners and the prize amount, which are also mentioned in the premise
# the hypothesis specifies the condition for winning, which is matching the five non-Mega ball numbers, which could be inferred as matching all numbers except the Mega ball in the premise
if winners_premise != winners_hypothesis:
    # check if the number of winners in the hypothesis contradicts the number of winners reported in the premise
    label = "contradiction"
elif prize_premise != prize_hypothesis:
    # check if the prize amount in the hypothesis contradicts the prize amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

