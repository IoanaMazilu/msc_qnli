# Premise: If Mel saved more than $10 by purchasing a sweater at a 15 percent discount, what is the smallest amount the original price of the sweater could be, to the nearest dollar?
# Hypothesis: If Mel saved more than $less than 30 by purchasing a sweater at a 15 percent discount, what is the smallest amount the original price of the sweater could be, to the nearest dollar?
# Golden Label: entailment

save_premise = 10
save_hypothesis = 30
discount = 15 / 100 # 15 percent discount

# the hypothesis refers to the amount saved and the discount mentioned in the premise
if save_hypothesis <= save_premise:
    # check if the amount saved in the hypothesis contradicts the amount saved in the premise
    label = "contradiction"
elif save_hypothesis / discount <= save_premise / discount:
    # check if the smallest original price of the sweater in the hypothesis contradicts the smallest original price of the sweater in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

