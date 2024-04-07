# Premise: Albert borrowed a total of $6000 from Brian and Charlie.
# Hypothesis: Albert borrowed a total of $more than 1000 from Brian and Charlie.
# Golden Label: entailment

borrowed_premise = 6000
borrowed_hypothesis = 1000

# the hypothesis talks about the total amount Albert borrowed, which is also mentioned in the premise
if borrowed_hypothesis >= borrowed_premise:
    # check if the hypothesis value contradicts the exact amount 'borrowed_premise' mentioned in the premise
    label = "contradiction"
elif borrowed_hypothesis > borrowed_premise:
    # check if the hypothesis contradicts the premise by stating more amount was borrowed
    label = "contradiction"
else:
    # any amount greater than 'borrowed_hypothesis' and less than or equal to 'borrowed_premise' is consistent with the premise
    # so we can infer entailment
    label = "entailment"

print(label)

