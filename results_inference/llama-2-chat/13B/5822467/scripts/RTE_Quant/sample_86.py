jobs_premise = 144000
jobs_hypothesis = 120000
unemployment_premise = 5.4
sector_hypothesis = 1/5

# the hypothesis talks about the proportion of new jobs created by a specific sector, which is not mentioned in the premise
# the hypothesis cannot be entailed from the premise, since the sector is not referenced
label = "neutral"

print(label)
