# define the minimum scores Roslin got in each step for both premise and hypothesis 
min_score_premise = [1, 2, 3, 4, 5]
min_score_hypothesis = [0, 2, 3, 4, 5] 

# define the condition of not getting the same score in consecutive steps for both premise and hypothesis
same_score_premise = False
same_score_hypothesis = False

# check if the minimum score in the hypothesis contradicts the minimum score in the premise
if min_score_hypothesis[0] >= min_score_premise[0]:
    label = "contradiction"
# check if the condition of not getting the same score in consecutive steps in the hypothesis contradicts the same condition in the premise
elif same_score_hypothesis != same_score_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
