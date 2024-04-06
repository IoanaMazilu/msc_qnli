# Premise: Craig Hicks, 46, was indicted on three counts of first-degree murder, according to the Durham County Clerk's office.
# Hypothesis: Clerk's office:Craig Hicks has been indicted on three counts of first-degree murder.
# Golden Label: entailment

counts_of_murder_premise = 3
counts_of_murder_hypothesis = 3

# the hypothesis mentions the number of counts of first-degree murder 
# for which Craig Hicks was indicted, which is also mentioned in the premise
if counts_of_murder_hypothesis != counts_of_murder_premise:
    # check if the number of counts of first-degree murder in the hypothesis contradicts 
    # the number of counts of first-degree murder in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

