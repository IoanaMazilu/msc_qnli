# Premise: Misha has 34.0 dollars and she receives 47.0 dollars more.
# Hypothesis: She has 78.0 dollars now.
# Golden Label: contradiction

initial_money_premise = 34.0
received_money_premise = 47.0
total_money_hypothesis = 78.0

# the hypothesis refers to the total amount of money, which is also mentioned in the premise
# compute the total money in the premise
total_money_premise = initial_money_premise + received_money_premise
if total_money_hypothesis != total_money_premise:
    # check if the total money in the hypothesis contradicts the total money from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

