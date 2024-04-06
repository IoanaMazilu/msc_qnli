# Premise: Paco had 93.0 cookies and Paco ate 15.0 of them.
# Hypothesis: Paco has 78.0 cookies left.
# Golden Label: entailment

initial_cookies_premise = 93.0
ate_cookies_premise = 15.0
left_cookies_hypothesis = 78.0

# the hypothesis refers to the number of cookies left, which can be computed from the premise
# compute the number of cookies left in the premise
left_cookies_premise = initial_cookies_premise - ate_cookies_premise
if left_cookies_hypothesis != left_cookies_premise:
    # check if the number of cookies left in the hypothesis contradicts the number of cookies left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

