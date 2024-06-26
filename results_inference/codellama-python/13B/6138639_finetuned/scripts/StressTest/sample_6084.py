ram_shyam_work_premise = 20
ram_shyam_work_hypothesis = 10

# the hypothesis talks about the number of days Ram and Shyam can do a piece of work together, referenced also in the premise
if ram_shyam_work_hypothesis >= ram_shyam_work_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ram_shyam_work_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of days
    # any number of days less than 'ram_shyam_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
