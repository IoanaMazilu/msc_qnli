# Premise: The first Barbie doll was sold for $3.
# Hypothesis: The first Barbie cost 3 dollars.
# Golden Label: entailment

doll_price_premise = 3
doll_price_hypothesis = 3

# the hypothesis talks about the cost of the first Barbie which is also mentioned in the premise
if doll_price_hypothesis != doll_price_premise:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # if the price in the hypothesis does not contradict the price in the premise, we can infer entailment
    label = "entailment"

print(label)

