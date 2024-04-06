# Premise: The City Council recently budgeted $7,300 to pay for training Officer Ron Inman and his dog Waldo.
# Hypothesis: The City Council paid $7,300 to train a dog.
# Golden Label: neutral

budgeted_amount_premise = 7300
budgeted_amount_hypothesis = 7300

# The hypothesis talks about the amount paid by the City Council for training a dog which is also mentioned in the premise
if budgeted_amount_hypothesis != budgeted_amount_premise:
    # Check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

