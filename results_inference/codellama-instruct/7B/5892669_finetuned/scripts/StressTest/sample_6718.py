aaron_jelly_premise = 7
aaron_jelly_hypothesis = 5
bianca_jelly_premise = 7
bianca_jelly_hypothesis = 7
callie_jelly_premise = 8
callie_jelly_hypothesis = 8
dante_jelly_premise = 13
dante_jelly_hypothesis = 13

# the hypothesis refers to the number of jelly beans each child has, as mentioned in the premise
if aaron_jelly_hypothesis >= aaron_jelly_premise:
    # check if the number of jelly beans Aaron has in the hypothesis contradicts the estimate of less than 'aaron_jelly_premise'
    label = "contradiction"
elif bianca_jelly_hypothesis!= bianca_jelly_premise:
    # check if the number of jelly beans Bianca has in the hypothesis contradicts the number of jelly beans Bianca has in the premise
    label = "contradiction"
elif callie_jelly_hypothesis!= callie_jelly_premise:
    # check if the number of jelly beans Callie has in the hypothesis contradicts the number of jelly beans Callie has in the premise
    label = "contradiction"
elif dante_jelly_hypothesis!= dante_jelly_premise:
    # check if the number of jelly beans Dante has in the hypothesis contradicts the number of jelly beans Dante has in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
