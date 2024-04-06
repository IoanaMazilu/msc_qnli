# Premise: Sara got fast food for lunch and Sara spent $5.36 on a hotdog and $5.1 on a salad.
# Hypothesis: The total of the lunch bill is 6.6.
# Golden Label: contradiction

hotdog_price_premise = 5.36
salad_price_premise = 5.1
total_lunch_bill_hypothesis = 6.6

# the hypothesis refers to the total of the lunch bill, which can be calculated from the premise
# compute the total of the lunch bill in the premise
total_lunch_bill_premise = hotdog_price_premise + salad_price_premise
if total_lunch_bill_hypothesis != total_lunch_bill_premise:
    # check if the total of the lunch bill in the hypothesis contradicts the total of the lunch bill from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

