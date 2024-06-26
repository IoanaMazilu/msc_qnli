people_iceland_norway_premise = 41
people_iceland_norway_hypothesis = 31

# the hypothesis talks about the number of people who have visited both Iceland and Norway, referenced in the premise
if people_iceland_norway_hypothesis >= people_iceland_norway_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif people_iceland_norway_hypothesis < people_iceland_norway_premise:
    # check if the hypothesis value is less than the premise value, which means the hypothesis entails the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
