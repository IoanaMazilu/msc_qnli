neha_premise = 10
neha_hypothesis = 60
both_premise = 15
both_hypothesis = 15
sadaf_tanu_premise = 10
sadaf_tanu_hypothesis = 10

# the hypothesis refers to the ages of Neha, Sonali, Priyanka, Sadaf and Tanu mentioned in the premise
if neha_hypothesis >= neha_premise:
    # check if the hypothesis value contradicts the age of Neha in the premise
    label = "contradiction"
elif both_hypothesis != both_premise:
    # check if the ages of Sonali and Priyanka in the hypothesis contradicts the ages of Sonali and Priyanka reported in the premise
    label = "contradiction"
elif sadaf_tanu_hypothesis != sadaf_tanu_premise:
    # check if the ages of Sadaf and Tanu in the hypothesis contradicts the ages of Sadaf and Tanu reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
