# Premise: Paco had 93.0 cookies and Paco ate 15.0 of them.
# Hypothesis: Paco has 77.0 cookies left.
# Golden Label: contradiction

initial_cookies_premise = 93.0
eaten_cookies_premise = 15.0
cookies_left_hypothesis = 77.0

# the hypothesis refers to the number of cookies left, which can be calculated from the premise
# compute the number of cookies left in the premise
cookies_left_premise = initial_cookies_premise - eaten_cookies_premise
if cookies_left_hypothesis != cookies_left_premise:
    # check if the number of cookies left in the hypothesis contradicts the number of cookies left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

