cakes_baked_lunch_premise = 5.0
cakes_sold_dinner_premise = 6.0
cakes_baked_yesterday_premise = 3.0
cakes_left_hypothesis = 3.0

# the hypothesis refers to the number of cakes left, which are also mentioned in the premise
# compute the total number of cakes sold and baked today
total_cakes_sold_today_premise = cakes_sold_dinner_premise
total_cakes_baked_today_premise = cakes_baked_lunch_premise

# compute the total number of cakes sold and baked yesterday
total_cakes_sold_yesterday_premise = 0
total_cakes_baked_yesterday_premise = cakes_baked_yesterday_premise

# compute the total number of cakes sold and baked today and yesterday
total_cakes_sold_premise = total_cakes_sold_today_premise + total_cakes_sold_yesterday_premise
total_cakes_baked_premise = total_cakes_baked_today_premise + total_cakes_baked_yesterday_premise

# check if the number of cakes left in the hypothesis contradicts the number of cakes sold and baked today and yesterday
if cakes_left_hypothesis!= total_cakes_sold_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
