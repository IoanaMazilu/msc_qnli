# John's tip percentage over the original price of the dish
john_tip_premise = 15
john_tip_hypothesis = 25

# Jane's tip percentage over the discounted price of the dish
jane_tip_premise = jane_tip_hypothesis = 15

# the hypothesis refers to the percentage of the tip John and Jane paid, which is also mentioned in the premise
if john_tip_premise!= john_tip_hypothesis:
    # check if the percentage of the tip John paid in the hypothesis contradicts the percentage of the tip John paid in the premise
    label = "contradiction"
elif jane_tip_premise!= jane_tip_hypothesis:
    # check if the percentage of the tip Jane paid in the hypothesis contradicts the percentage of the tip Jane paid in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
