n=raw_input()
grades = []
for entry in range(int(n)):
    grades.append([i for i in raw_input().split()])
query = raw_input()

# Find list where first item matches name in query and
# assign grades to queryResult
queryResult = [x[1:] for x in grades if x[0] == query]

total = 0
scores = 0
for x in queryResult:
    for y in x:
        total += float(y)
        scores += 1
print "%.2f" % (float(total/scores))
