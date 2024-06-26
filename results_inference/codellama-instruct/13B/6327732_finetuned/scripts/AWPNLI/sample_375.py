baked_cakes_lunch_premise = 5.0
sold_cakes_dinner_premise = 6.0
baked_cakes_yesterday_premise = 3.0

# the hypothesis refers to the number of cakes left, which are also mentioned in the premise
# compute the total number of cakes baked and sold today
total_cakes_today_premise = baked_cakes_lunch_premise + sold_cakes_dinner_premise
# compute the total number of cakes baked yesterday
total_cakes_yesterday_premise = baked_cakes_yesterday_premise
# compute the number of cakes left today
cakes_left_today_premise = total_cakes_today_premise - total_cakes_yesterday_premise

# check if the number of cakes left today contradicts the number of cakes left in the hypothesis
if cakes_left_today_premise!= 3.0:
    label = "contradiction"
else:
    label = "entailment"

print(label)
