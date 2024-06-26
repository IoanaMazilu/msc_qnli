served_hamburgers_premise = 3.0
made_hamburgers_premise = 9.0
left_over_hamburgers_hypothesis = 6.0

# the hypothesis talks about the number of hamburgers left over, which is also referenced in the premise
# compute the number of hamburgers actually served from the premise
served_hamburgers_premise = made_hamburgers_premise - served_hamburgers_premise
if left_over_hamburgers_hypothesis!= served_hamburgers_premise:
    # check if the number of hamburgers left over from the hypothesis contradicts the number of hamburgers served from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
