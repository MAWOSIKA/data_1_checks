schedule_file = open('schedule.txt', 'r')
for line in schedule_file:
    
    print(line)
schedule_file.close()
(show, time) = line.split(' - ')
print(show, time)
