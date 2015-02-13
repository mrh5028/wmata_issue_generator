import random
from csv import reader

lines = ["Orange", "Red", "Green","Yellow","Blue","Silver"]

def issue_maker():
    sent_type = random.randint(1,3)
    sent_complete = ""
    #1 - Line Issue
    #2 - Station Issue
    #3 - System Issue
    if sent_type == 1:
        sent_complete = line_issue_sent()
    elif sent_type == 2:
        sent_complete = station_issue_sent()
    elif sent_type == 3:
        sent_complete = system_issue_sent()
    return sent_complete

def line_issue_sent(): #The <line> is <issue>
    with open('line_issues.txt', 'r') as f:
        issues = [line.strip() for line in f]
    f.close()
    
    print_line = random.choice(lines)
    print_issue = random.choice(issues)
    
    sent = "The %s line is %s."  % (print_line, print_issue)
    return sent
    
def station_issue_sent(): #Expect delays on the <line> due to <issue> at <station>
    with open('station_lines.csv',mode='rU') as infile:
        station_lines = dict(reader(infile))
    
    with open('station_issues.txt', 'r') as f:
        issues = [line.strip() for line in f]
    f.close()
    
    print_issue = random.choice(issues)
    print_station = random.choice(station_lines.keys())
    print_line = station_lines.get(print_station, 0)
    
    
    sent = "Expect delays on the %s due to %s at %s." % (print_line, print_issue, print_station)
    return sent

def system_issue_sent(): #Metro is experiencing system-wide delays due to <issue>
    with open('system_issues.txt', 'r') as f:
        issues = [line.strip() for line in f]
    f.close()
    
    print_issue = random.choice(issues)
    
    sent = "Metro is experiencing system-wide delays due to %s."  % (print_issue)
    return sent
print issue_maker()