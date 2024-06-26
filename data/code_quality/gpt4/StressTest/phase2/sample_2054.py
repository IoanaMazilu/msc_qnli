purchase_price_premise = 9/10
purchase_price_hypothesis = 9/10
selling_price_increase_premise = 0.08
selling_price_increase_hypothesis = 0.08

# the hypothesis talks about the purchase price and selling price increase of a pressure cooker, referenced also in the premise
if purchase_price_hypothesis > purchase_price_premise:
    # check if the hypothesis value contradicts the given purchase price in the premise
    label = "contradiction"
elif selling_price_increase_hypothesis != selling_price_increase_premise:
    # check if the selling price increase in the hypothesis contradicts the selling price increase reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
