# Premise: Mr Vishwas got an amount of 10920 as an interest at the end of eight years.
# Hypothesis: Mr Vishwas got an amount of 20920 as an interest at the end of eight years.
# Golden Label: contradiction

interest_premise = 10920
interest_hypothesis = 20920

# the hypothesis talks about the interest amount received by Mr Vishwas, also mentioned in the premise
if interest_hypothesis != interest_premise:
    # check if the interest amount in the hypothesis contradicts the actual interest amount in the premise
    label = "contradiction"
else:
    # if the interest amount in the hypothesis does not contradict the interest amount in the premise, we can infer entailment
    label = "entailment"

print(label)

