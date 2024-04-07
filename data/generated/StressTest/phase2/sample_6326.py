# Premise: In an exam, Bobby scored 38 percent, Bonny scored 56 percent, Vijay scored 66 percent and Libin scored 75 percent.
# Hypothesis: In an exam, Bobby scored 88 percent, Bonny scored 56 percent, Vijay scored 66 percent and Libin scored 75 percent.
# Golden Label: contradiction

bobby_score_premise = 38
bonny_score_premise = 56
vijay_score_premise = 66
libin_score_premise = 75

bobby_score_hypothesis = 88
bonny_score_hypothesis = 56
vijay_score_hypothesis = 66
libin_score_hypothesis = 75

# the hypothesis refers to the scores of four individuals mentioned in the premise 
if bobby_score_premise != bobby_score_hypothesis:
    # check if the score of Bobby in the hypothesis contradicts his score in the premise
    label = "contradiction"
elif bonny_score_premise != bonny_score_hypothesis or vijay_score_premise != vijay_score_hypothesis or libin_score_premise != libin_score_hypothesis:
    # check if the scores of Bonny, Vijay, or Libin in the hypothesis contradict their respective scores in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

