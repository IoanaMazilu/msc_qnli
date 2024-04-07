# Premise: Mr Vishwas got an amount of 10920 as an interest at the end of eight years.
# Hypothesis: Mr Vishwas got an amount of less than 80920 as an interest at the end of eight years.
# Golden Label: entailment

interest_premise = 10920
interest_hypothesis = 80920

# the hypothesis talks about the amount of interest Mr Vishwas got, referenced also in the premise
if interest_hypothesis <= interest_premise:
    # check if the hypothesis value contradicts the amount of interest in the premise
    label = "contradiction"
else:
    # if the hypothesis value is higher than the premise, but not contradictory, we can infer entailment
    label = "entailment"

print(label)

