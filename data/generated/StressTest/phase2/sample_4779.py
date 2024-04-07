# Premise: If Elena purchased a total of 12 of these pens for $42.00, how many brand X pens did she purchase?
# Hypothesis: If Elena purchased a total of less than 52 of these pens for $42.00, how many brand X pens did she purchase?
# Golden Label: entailment

pens_purchased_premise = 12
pens_purchased_hypothesis = 52
price_premise = 42
price_hypothesis = 42

# the hypothesis refers to the number of pens purchased by Elena and the price, mentioned in the premise
if pens_purchased_hypothesis <= pens_purchased_premise and price_hypothesis == price_premise:
    # check if 'pens_purchased_hypothesis' contradicts the number of pens purchased in the premise
    label = "contradiction"
elif price_hypothesis != price_premise:
    # check if the price in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

