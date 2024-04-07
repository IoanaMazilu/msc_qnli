# Premise: Albert completes a piece of work in less than 50 days, Rose completes the same work in 30 days.
# Hypothesis: Albert completes a piece of work in 20 days, Rose completes the same work in 30 days.
# Golden Label: neutral

Albert_work_premise = 50
Albert_work_hypothesis = 20
Rose_work_premise = 30
Rose_work_hypothesis = 30

# the hypothesis refers to the time Albert and Rose need to complete a piece of work, also mentioned in the premise
if Albert_work_hypothesis >= Albert_work_premise:
    # check if the time Albert needs in the hypothesis contradicts the upper limit given in the premise
    label = "contradiction"
elif Rose_work_hypothesis != Rose_work_premise:
    # check if the time Rose needs in the hypothesis contradicts the time Rose needs in the premise
    label = "contradiction"
else:
    # the premise gives only an upper limit for the time Albert needs
    # the time 'Albert_work_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

