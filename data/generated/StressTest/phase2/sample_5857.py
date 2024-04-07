# Premise: If Elena purchased a total of less than 30 of these pens for $42.00, how many brand X pens did she purchase?
# Hypothesis: If Elena purchased a total of 10 of these pens for $42.00, how many brand X pens did she purchase?
# Golden Label: neutral

total_pens_premise = 30
total_pens_hypothesis = 10

# the hypothesis is talking about the total number of pens purchased by Elena, which is also mentioned in the premise
if total_pens_hypothesis >= total_pens_premise:
    # check if the total number of pens in the hypothesis contradicts the less than 'total_pens_premise' in the premise
    label = "contradiction"
elif total_pens_hypothesis < total_pens_premise:
    # the number of pens in the hypothesis is less than 'total_pens_premise', it does not contradict the premise
    # but the exact number cannot be explicitly entailed from the premise, so it's neutral
    label = "neutral"

print(label)

