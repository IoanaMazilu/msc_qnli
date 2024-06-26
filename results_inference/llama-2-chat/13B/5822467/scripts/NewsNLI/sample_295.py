rent_premise = 613
popular_categories_premise = ["sales", "customer service", "management"]

# define variables for the hypothesis
rent_hypothesis = 613

# check if the hypothesis mentions any new information not present in the premise
if popular_categories_hypothesis!= popular_categories_premise:
    # if the hypothesis mentions new categories not present in the premise, the labels are neutral
    label = "neutral"
elif rent_hypothesis!= rent_premise:
    # if the hypothesis mentions a different rent amount, the labels are contradiction
    label = "contradiction"
else:
    # if the hypothesis mentions the same rent amount as the premise, we can infer entailment
    label = "entailment"

print(label)
