# define variables for the numerical entities in the premise and hypothesis
premise_wins = 1
hypothesis_wins = 1
premise_no = 1
hypothesis_no = 1

# check if the number of wins in the hypothesis contradicts the number of wins in the premise
if hypothesis_wins!= premise_wins:
    label = "contradiction"
# check if the number of European No. in the hypothesis contradicts the number of European No. in the premise
elif hypothesis_no!= premise_no:
    label = "contradiction"
# if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
else:
    label = "entailment"

print(label)
