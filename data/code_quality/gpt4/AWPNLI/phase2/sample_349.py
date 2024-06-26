friday_visitors_premise = 1250.0
multiplier_premise = 3.0
saturday_visitors_hypothesis = 3748.0

# the hypothesis refers to the number of people who visited the zoo on Saturday, which is also mentioned in the premise
# compute the number of people who visited the zoo on Saturday according to the premise
saturday_visitors_premise = friday_visitors_premise * multiplier_premise
if saturday_visitors_hypothesis != saturday_visitors_premise:
    # check if the number of Saturday visitors in the hypothesis contradicts the number of Saturday visitors from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
