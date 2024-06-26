# The hypothesis and premise talk about the on-time departure rate of flights from Phoenix
# Both the hypothesis and premise are referring to the same situation

# the hypothesis mentions an on-time departure rate of 70%
# the premise mentions an on-time departure rate of less than 80%

if hypothesis_departure_rate < 80:
    # the premise mentions an on-time departure rate of less than 80%
    # this is contradicting the hypothesis which states an on-time departure rate of 70%
    label = "contradiction"
elif hypothesis_departure_rate > 70:
    # the hypothesis states an on-time departure rate of 70%
    # the premise does not contradict this, so we can infer entailment
    label = "entailment"
else:
    # the hypothesis and premise are identical
    # so if the hypothesis_departure_rate is equal to the premise_departure_rate,
    # we have a neutral relation
    label = "neutral"

print(label)
