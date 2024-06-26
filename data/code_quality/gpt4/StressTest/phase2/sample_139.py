chocolates_premise = 200
chocolates_hypothesis = 500

# the hypothesis talks about the number of chocolates Shreehari has, referenced also in the premise
if chocolates_hypothesis <= chocolates_premise:
    # check if the hypothesis value contradicts the estimate of more than 'chocolates_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of chocolates
    # any number of chocolates greater than 'chocolates_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
