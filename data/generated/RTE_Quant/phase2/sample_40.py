# Premise: The World Court, or International Court of Justice (ICJ), located in The Hague, is made up of fifteen permanent judges plus two judges nominated by the parties involved in the dispute under consideration.
# Hypothesis: Two judges of the ICJ are nominated by the parties involved.
# Golden Label: entailment

total_judges_premise = 15
additional_judges_premise = 2
additional_judges_hypothesis = 2

# the hypothesis talks about the number of additional judges nominated by the parties involved, which is also mentioned in the premise
if additional_judges_hypothesis != additional_judges_premise:
    # check if the number of additional judges in the hypothesis contradicts the number of additional judges from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

