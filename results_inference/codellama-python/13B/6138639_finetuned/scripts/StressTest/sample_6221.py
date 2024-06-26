priya_ratio_premise = 2
mani_ratio_premise = 4
rani_ratio_premise = 8
priya_ratio_hypothesis = 2
mani_ratio_hypothesis = 4
rani_ratio_hypothesis = 8

# the hypothesis refers to the ratio of money to be divided between Priya, Mani and Rani, mentioned in the premise
if priya_ratio_hypothesis >= priya_ratio_premise:
    # check if the estimate of 'priya_ratio_hypothesis' contradicts the ratio of money to Priya in the premise
    label = "contradiction"
elif mani_ratio_hypothesis >= mani_ratio_premise:
    # check if the estimate of'mani_ratio_hypothesis' contradicts the ratio of money to Mani in the premise
    label = "contradiction"
elif rani_ratio_hypothesis >= rani_ratio_premise:
    # check if the estimate of 'rani_ratio_hypothesis' contradicts the ratio of money to Rani in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
