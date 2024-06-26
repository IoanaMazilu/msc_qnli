suresh_average_premise = 55
suresh_average_hypothesis = 35

# the hypothesis talks about the average marks of Suresh in English and History, which is also mentioned in the premise
if suresh_average_hypothesis!= suresh_average_premise:
    # check if the average marks in the hypothesis contradicts the average marks in the premise
    label = "contradiction"
else:
    # if the average marks in the hypothesis does not contradict the average marks in the premise, we can infer entailment
    label = "entailment"

print(label)
