# Premise: If Tom received $more than 400 more than Jerry did, what was the profit made by their business in that year?
# Hypothesis: If Tom received $800 more than Jerry did, what was the profit made by their business in that year?
# Golden Label: neutral

profit_difference_premise = 400
profit_difference_hypothesis = 800

# the hypothesis talks about the profit difference between Tom and Jerry, referenced also in the premise
if profit_difference_hypothesis <= profit_difference_premise:
    # check if the hypothesis value contradicts the estimate of more than 'profit_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the profit difference
    # any profit difference greater than 'profit_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

