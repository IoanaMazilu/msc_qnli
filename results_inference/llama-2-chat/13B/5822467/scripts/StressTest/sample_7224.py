oa_premise = 2
ac_premise = 4
bd_premise = 6

# define variables for the hypothesis
oa_hypothesis = 5
ac_hypothesis = 4
bd_hypothesis = 6

# calculate the length of OB based on the hypothesis
ob_hypothesis = oa_hypothesis + ac_hypothesis + bd_hypothesis

# compare the premise and hypothesis values
if oa_premise <= oa_hypothesis:
    # check if the estimate of 'oa_hypothesis' contradicts the value of OA in the premise
    label = "contradiction"
elif ac_premise!= ac_hypothesis:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
elif bd_premise!= bd_hypothesis:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

# calculate the length of OB based on the hypothesis
ob_hypothesis = oa_hypothesis + ac_hypothesis + bd_hypothesis

print(label)
