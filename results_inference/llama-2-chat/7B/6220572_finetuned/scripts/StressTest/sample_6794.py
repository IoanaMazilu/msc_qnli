dibi_percent_premise = 25
dibi_percent_hypothesis = 25
balan_percent_premise = 38
balan_percent_hypothesis = 38
cristen_percent_premise = 23
cristen_percent_hypothesis = 23

# the hypothesis refers to the percentages of scores for Dibi, Balan, and Cristen in the premise
if dibi_percent_hypothesis >= dibi_percent_premise:
    # check if the estimate of 'dibi_percent_hypothesis' contradicts the percentage of score for Dibi in the premise
    label = "contradiction"
elif balan_percent_hypothesis!= balan_percent_premise:
    # check if the percentage of score for Balan in the hypothesis contradicts the percentage of score for Balan reported in the premise
    label = "contradiction"
elif cristen_percent_hypothesis!= cristen_percent_premise:
    # check if the percentage of score for Cristen in the hypothesis contradicts the percentage of score for Cristen reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
