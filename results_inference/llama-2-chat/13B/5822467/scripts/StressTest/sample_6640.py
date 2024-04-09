ram_krish_premise = 20
ram_krish_hypothesis = 40
bhim_premise = None

# the hypothesis talks about the time taken by Ram and Krish together, which is also mentioned in the premise
if ram_krish_hypothesis <= ram_krish_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ram_krish_premise'
    label = "contradiction"
elif bhim_premise is not None and bhim_premise > ram_krish_hypothesis:
    # check if the estimate of Bhim's time contradicts the time taken by Ram and Krish
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
