kilometers_premise = 25.0
kilometers_per_hour_premise = 5.0
hours_hypothesis = 4.0

# the hypothesis refers to the number of kilometers and the speed, which are also mentioned in the premise
# compute the total number of kilometers in the premise
total_kilometers_premise = kilometers_premise / kilometers_per_hour_premise * hours_hypothesis
if total_kilometers_hypothesis!= total_kilometers_premise:
    # check if the number of kilometers in the hypothesis contradicts the number of kilometers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
