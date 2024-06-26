years_future = 5
years_hypothesis = 2

# the hypothesis talks about Arun's age after a certain number of years,
# which is also mentioned in the premise
if years_hypothesis >= years_future:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, we can infer entailment
    label = "entailment"

print(label)
