anwar_sales_premise = 3600
anwar_sales_hypothesis = 3600
interest_rate_premise = 6
interest_rate_hypothesis = 6

# the hypothesis talks about the number of Anwar's sales, referenced also in the premise
if anwar_sales_hypothesis <= anwar_sales_premise:
    # check if the hypothesis value contradicts the number of Anwar's sales reported in the premise
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
