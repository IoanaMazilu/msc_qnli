anwar_sales_premise = 3600
anwar_sales_hypothesis = float("+inf")

# the hypothesis talks about the sales of Anwar, referenced also in the premise
if anwar_sales_premise <= anwar_sales_hypothesis:
    # check if the estimate of 'anwar_sales_hypothesis' contradicts the number of sales reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of sales
    # any number of sales greater than 'anwar_sales_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
