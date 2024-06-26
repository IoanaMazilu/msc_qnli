priya_mani_raio_premise = 4/8
priya_mani_raio_hypothesis = 2/4

# the hypothesis talks about the ratio of money to be divided between Priya, Mani and Rani, referenced also in the premise
if priya_mani_raio_hypothesis >= priya_mani_raio_premise:
    # check if the hypothesis value contradicts the estimate of less than 'priya_mani_raio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of money
    # any ratio less than 'priya_mani_raio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
