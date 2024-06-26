premise_lunch = 5.0
premise_dinner = 6.0
premise_yesterday = 3.0
hypothesis = 3.0

# the hypothesis refers to the number of cakes left, which are also mentioned in the premise
# compute the total number of cakes sold today
total_cakes_sold_today = premise_lunch + premise_dinner

# check if the number of cakes left in the hypothesis contradicts the number of cakes sold today
if hypothesis > total_cakes_sold_today:
    label = "contradiction"
else:
    label = "entailment"

print(label)
