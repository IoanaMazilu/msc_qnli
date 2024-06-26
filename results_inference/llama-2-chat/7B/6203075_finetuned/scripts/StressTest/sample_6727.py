apples_premise = 20
apples_hypothesis = 10

# the hypothesis talks about the number of apples and oranges selected by Mary, which is also mentioned in the premise
if apples_hypothesis >= apples_premise:
    # check if the number of apples and oranges in the hypothesis contradicts the estimate of less than 'apples_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples and oranges
    # any number of apples and oranges less than 'apples_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
