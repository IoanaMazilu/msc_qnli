john_tip_premise = 85
john_tip_hypothesis = 15
jane_tip_premise = "discounted price" #no numerical data given
jane_tip_hypothesis = "discounted price" #no numerical data given

# the hypothesis refers to the percentage of the tip John paid, which is also mentioned in the premise
if john_tip_hypothesis >= john_tip_premise:
    # check if the amount of 'john_tip_hypothesis' contradicts the estimate of less than 'john_tip_premise' reported in the premise
    label = "contradiction"
elif jane_tip_hypothesis != jane_tip_premise:
    # check if Jane's payment method in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
