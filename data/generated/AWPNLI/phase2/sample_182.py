# Premise: Mrs. Hilt has 50.0 cents and a pencil costs 5.0 cents.
# Hypothesis: She can buy 10.0 pencils with the money she has.
# Golden Label: entailment

cents_premise = 50.0
pencil_cost_premise = 5.0
pencils_hypothesis = 10.0

# the hypothesis makes a claim about the number of pencils Mrs. Hilt can buy, which depends on the number of cents she has and the cost of each pencil
# compute the maximum number of pencils she can buy as per the premise
max_pencils_premise = cents_premise / pencil_cost_premise
if pencils_hypothesis != max_pencils_premise:
    # check if the number of pencils from the hypothesis contradicts the maximum number of pencils Mrs. Hilt can buy according to the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

