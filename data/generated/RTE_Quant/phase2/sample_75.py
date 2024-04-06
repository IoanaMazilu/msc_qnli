# Premise: There are 360 million European citizens in 15 member states and yet we can not find just 20 men and women with the relevant professional competence and work experience to be commissioners.
# Hypothesis: There are 360 million European citizens.
# Golden Label: entailment

citizens_premise = 360e6
citizens_hypothesis = 360e6

# the hypothesis talks about the number of European citizens, which is also mentioned in the premise
if citizens_hypothesis != citizens_premise:
    # check if the number of European citizens in the hypothesis contradicts the number of European citizens from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

