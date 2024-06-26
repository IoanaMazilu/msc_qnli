# define variables for the relevant information in the premise and hypothesis
premise_men = 3
hypothesis_men = 3
premise_torture = True
hypothesis_torture = True

# check if the number of men in the hypothesis contradicts the number of men in the premise
if hypothesis_men!= premise_men:
    label = "contradiction"
# check if the torture information in the hypothesis contradicts the torture information in the premise
elif hypothesis_torture!= premise_torture:
    label = "contradiction"
# if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
else:
    label = "entailment"

print(label)
