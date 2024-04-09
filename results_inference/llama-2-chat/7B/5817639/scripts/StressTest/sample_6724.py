anwar_sales_premise = 1600
anwar_sales_hypothesis = 3600

# the hypothesis talks about the total sales of Anwar, which is also mentioned in the premise
if anwar_sales_hypothesis <= anwar_sales_premise:
    # check if the hypothesis value contradicts the estimate of 'anwar_sales_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total sales of Anwar
    # any total sales greater than 'anwar_sales_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
