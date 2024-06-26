picked_apples_mike_premise = 7.0
ate_apples_nancy_premise = 3.0
picked_apples_keith_premise = 6.0
picked_pears_keith_premise = 4.0
left_apples_hypothesis = 10.0

# the hypothesis refers to the number of apples left, which is related to the number of apples picked and eaten in the premise
# compute the total number of apples in the premise
total_apples_premise = picked_apples_mike_premise + picked_apples_keith_premise - ate_apples_nancy_premise
if left_apples_hypothesis != total_apples_premise:
    # check if the number of apples left in the hypothesis contradicts the number of apples from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
