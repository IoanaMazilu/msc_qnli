# Premise: Sue’s mother made 75.0 cookies and she put the cookies in bags, with 3.0 cookies in each bag.
# Hypothesis: She could fill up 20.0 bags.
# Golden Label: contradiction

made_cookies_premise = 75.0
cookies_per_bag_premise = 3.0
filled_bags_hypothesis = 20.0

# the hypothesis refers to the number of filled bags, which can be estimated from the number of cookies made and the number of cookies per bag in the premise
# compute the number of filled bags in the premise
filled_bags_premise = made_cookies_premise / cookies_per_bag_premise
if filled_bags_hypothesis != filled_bags_premise:
    # check if the number of filled bags in the hypothesis contradicts the number of filled bags from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

