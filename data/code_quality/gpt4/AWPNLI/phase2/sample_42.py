hotdog_premise = 5.36
salad_premise = 5.1
total_lunch_bill_hypothesis = 10.46

# the hypothesis refers to the total lunch bill, which is also mentioned in the premise
# compute the total lunch bill in the premise
total_lunch_bill_premise = hotdog_premise + salad_premise
if total_lunch_bill_hypothesis != total_lunch_bill_premise:
    # check if the total lunch bill in the hypothesis contradicts the total lunch bill from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
