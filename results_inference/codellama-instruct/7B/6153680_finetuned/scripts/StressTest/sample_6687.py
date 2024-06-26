# Define the variables for the premise and hypothesis
purchased_copies_premise = 60
hardback_copies_premise = 10
hardback_price_premise = 20
paperback_copies_premise = purchased_copies_premise - hardback_copies_premise
paperback_price_premise = 10

purchased_copies_hypothesis = 40
hardback_copies_hypothesis = 10
hardback_price_hypothesis = 20
paperback_copies_hypothesis = purchased_copies_hypothesis - hardback_copies_hypothesis
paperback_price_hypothesis = 10

# The hypothesis refers to the number of copies purchased, which is also mentioned in the premise
if purchased_copies_hypothesis > purchased_copies_premise:
    # Check if the number of copies purchased in the hypothesis contradicts the number of copies purchased in the premise
    label = "contradiction"
else:
    # If the number of copies purchased in the hypothesis does not contradict the number of copies purchased in the premise, we can infer entailment
    label = "entailment"

print(label)
