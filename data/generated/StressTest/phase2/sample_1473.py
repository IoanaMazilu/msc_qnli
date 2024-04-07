# Premise: Raju has scored 250 marks and was declared failed by 22 marks.
# Hypothesis: Raju has scored less than 650 marks and was declared failed by 22 marks.
# Golden Label: entailment

marks_scored_premise = 250
marks_scored_hypothesis = 650
marks_failed_premise = 22
marks_failed_hypothesis = 22

# the hypothesis talks about the score of Raju and the marks he failed by, both referenced in the premise
if marks_scored_premise >= marks_scored_hypothesis:
    # check if the estimate of 'marks_scored_hypothesis' contradicts the score in the premise
    label = "contradiction"
elif marks_failed_hypothesis != marks_failed_premise:
    # check if the number of marks failed by in the hypothesis contradicts the number of marks failed by reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

