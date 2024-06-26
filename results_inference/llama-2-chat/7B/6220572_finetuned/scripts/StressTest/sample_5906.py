# the hypothesis refers to the number of cookies eaten by Michael, Steve and Tyler
# the premise gives the number of cookies eaten by Michael and Steve

# check if the hypothesis value contradicts the number of cookies eaten by Michael and Steve in the premise
if cookie_sales_hypothesis <= cookie_sales_premise:
    label = "contradiction"
elif pies_sold_hypothesis!= pies_sold_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
