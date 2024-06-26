potential_jurors_premise = 84
potential_jurors_hypothesis = 84
african_americans_premise = 6
african_americans_hypothesis = 6

# the hypothesis mentions the pool of 84 potential jurors in court, which is also mentioned in the premise
# the hypothesis also mentions six jurors who are African-American, which is also mentioned in the premise
if potential_jurors_hypothesis!= potential_jurors_premise:
    # check if the number of potential jurors from the hypothesis contradicts the number of potential jurors in the premise
    label = "contradiction"
elif african_americans_hypothesis!= african_americans_premise:
    # check if the number of African-Americans from the hypothesis contradicts the number of African-Americans in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
