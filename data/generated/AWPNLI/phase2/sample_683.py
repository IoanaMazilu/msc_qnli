# Premise: George had 28.0 socks, and he bought 36.0 new ones and his Dad gave him 4.0 more.
# Hypothesis: He would have 69.0 socks.
# Golden Label: contradiction

initial_socks_premise = 28.0
bought_socks_premise = 36.0
gifted_socks_premise = 4.0
total_socks_hypothesis = 69.0

# the hypothesis refers to the total number of socks, which is also calculated in the premise
# compute the total number of socks in the premise
total_socks_premise = initial_socks_premise + bought_socks_premise + gifted_socks_premise
if total_socks_hypothesis != total_socks_premise:
    # check if the total number of socks in the hypothesis contradicts the total number of socks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

