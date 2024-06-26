# the hypothesis talks about the number of tables needed, which is also referenced in the premise
# find the total number of people from the premise 
total_people_premise = 18.0 + 12.0
if total_people_premise >= 10.0:
    # check if the total people from the hypothesis contradict the estimate of more than '12.0'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
