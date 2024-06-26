earthquake_year_premise = 1994
earthquake_year_hypothesis = 1994

# the hypothesis talks about an earthquake happening in a certain year, which is also mentioned in the premise
if earthquake_year_hypothesis != earthquake_year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the year in the hypothesis does not contradict the year in the premise, we can infer entailment
    label = "entailment"

print(label)
