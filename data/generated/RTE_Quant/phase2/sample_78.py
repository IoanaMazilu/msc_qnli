# Premise: For the year, the Dow rose 3 percent, while the S & P 500 index added 9 percent.
# Hypothesis: For the year, the Dow gained 3 percent, the S & P rose 9 percent.
# Golden Label: entailment

dow_increase_premise = 3
dow_increase_hypothesis = 3
sp_increase_premise = 9
sp_increase_hypothesis = 9

# the hypothesis talks about the percentage increase of the Dow and the S & P, which is also mentioned in the premise
if dow_increase_hypothesis != dow_increase_premise:
    # check if the Dow increase percentage in the hypothesis contradicts the Dow increase percentage from the premise
    label = "contradiction"
elif sp_increase_hypothesis != sp_increase_premise:
    # check if the S & P increase percentage in the hypothesis contradicts the S & P increase percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

