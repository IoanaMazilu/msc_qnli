price_slump_premise = 68
price_slump_hypothesis = 28
price_rise_premise = 5
price_rise_hypothesis = 5

# the hypothesis refers to the price slump and rise mentioned in the premise
if price_slump_hypothesis >= price_slump_premise:
    # check if the price slump percentage in the hypothesis contradicts the estimate of less than 'price_slump_premise'
    label = "contradiction"
elif price_rise_hypothesis!= price_rise_premise:
    # check if the price rise percentage in the hypothesis contradicts the price rise percentage reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the price slump percentage
    # any percentage less than 'price_slump_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
