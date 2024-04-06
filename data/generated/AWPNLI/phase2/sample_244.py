# Premise: Sue’s mother made 75.0 cookies and she put the cookies in bags, with 3.0 cookies in each bag.
# Hypothesis: She could fill up 25.0 bags.
# Golden Label: entailment

made_cookies_premise = 75.0
cookies_per_bag_premise = 3.0
filled_bags_hypothesis = 25.0

# the hypothesis refers to the number of bags that could be filled, which can be inferred from the premise
# compute the number of bags that can be filled according to the premise
filled_bags_premise = made_cookies_premise / cookies_per_bag_premise
if filled_bags_hypothesis != filled_bags_premise:
    # check if the number of filled bags in the hypothesis contradicts the number of bags that could be filled according to the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

