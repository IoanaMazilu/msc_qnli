# the premise is referring to the same scenario as the hypothesis
if reema_marks_written_as_50:
    # the hypothesis refers to a specific scenario that can be inferred from the premise
    if reema_marks_written_as_less_than_60:
        # the hypothesis contradicts the premise, as the premise does not mention any specific marks written
        label = "contradiction"
    else:
        # the premise does not provide any information about the marks written, so the hypothesis is neutral
        label = "neutral"
else:
    # the premise is referring to the same scenario as the hypothesis, but the hypothesis does not make any reference to the premise
    label = "neutral"

print(label)
