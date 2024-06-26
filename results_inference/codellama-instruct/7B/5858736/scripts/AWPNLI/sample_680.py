# define variables with representative names for the numerical entities in both inputs
tickets_won_premise = 49.0
tickets_lost_premise = 6.0
tickets_spent_premise = 25.0
tickets_hypothesis = 18.0

# extract all quantities as valid numbers (integers or floats)
total_tickets_premise = tickets_won_premise - tickets_lost_premise + tickets_spent_premise

# use brief comments to explain what comparison you do between the defined variables
# find the total number of tickets from the premise
if total_tickets_premise >= tickets_hypothesis:
    # check if the total tickets from the hypothesis contradict the estimate of more than 'tickets_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
