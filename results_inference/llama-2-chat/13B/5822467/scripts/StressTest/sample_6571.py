vikas_rank_premise = 7
tanvi_rank_premise = 17

# define variables for the hypothesis
vikas_rank_hypothesis = 9
tanvi_rank_hypothesis = 17

# compare the premise and hypothesis values
if vikas_rank_hypothesis > vikas_rank_premise:
    # the hypothesis value is greater than the premise value, so there is entailment
    label = "entailment"
elif tanvi_rank_hypothesis == tanvi_rank_premise:
    # the hypothesis value is the same as the premise value, so there is no contradiction or entailment
    label = "neutral"
else:
    # the hypothesis value is less than the premise value, so there is contradiction
    label = "contradiction"

print(label)
