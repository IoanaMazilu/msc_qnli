# Premise: The pool of 84 potential jurors in court appeared diverse, although only six were African-American.
# Hypothesis: 84 potential jurors, including six African-Americans, remain in the jury pool.
# Golden Label: neutral

total_jurors_premise = 84
total_jurors_hypothesis = 84
african_american_jurors_premise = 6
african_american_jurors_hypothesis = 6

# the hypothesis mentions the total number of jurors and the number of African-American jurors, which are also mentioned in the premise
if total_jurors_hypothesis != total_jurors_premise:
    # check if the total number of jurors in the hypothesis contradicts the total number of jurors reported in the premise
    label = "contradiction"
elif african_american_jurors_hypothesis != african_american_jurors_premise:
    # check if the number of African-American jurors from the hypothesis contradicts the number of African-American jurors in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

