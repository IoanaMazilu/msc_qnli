# Premise: Only four countries have paid anything at all:Brazil, Norway, Estonia and Australia.
# Hypothesis: Only four countries have delivered any money at all.
# Golden Label: entailment

countries_paid_premise = 4
countries_paid_hypothesis = 4

# the hypothesis mentions the number of countries that have paid, which is also mentioned in the premise
if countries_paid_hypothesis != countries_paid_premise:
    # check if the number of countries that have paid in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

