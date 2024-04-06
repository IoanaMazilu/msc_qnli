# Premise: Sara got fast food for lunch and Sara spent $5.36 on a hotdog and $5.1 on a salad.
# Hypothesis: The total of the lunch bill is 5.6.
# Golden Label: contradiction

hotdog_price_premise = 5.36
salad_price_premise = 5.1
total_bill_hypothesis = 5.6

# the hypothesis refers to the total bill, which is also mentioned in the premise
# compute the total bill in the premise
total_bill_premise = hotdog_price_premise + salad_price_premise
if total_bill_hypothesis != total_bill_premise:
    # check if the total bill in the hypothesis contradicts the total bill from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

