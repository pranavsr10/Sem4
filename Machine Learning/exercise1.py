file= open('mbox-short.txt','r')
h = f.read()
file.close()

def number_of_lines():
    lines = h.split('\n')
    return(len(lines))

print(number_of_lines())
print()

def count_number_of_lines():
    lines = h.split('\n')
    counter = 0
    for i in lines:
        if i.startswith('Subject:'):
            counter+=1
    return counter

print(count_number_of_lines())
print()

def average_spam_confidence():
    lines = h.split('\n')
    avg_spam = 0
    ctr = 0
    for i in lines:
        if i.startswith('X-DSPAM-Confidence:'):
            avg_spam += float(i.split(': ')[1])
            ctr += 1
    return avg_spam/ctr

print(average_spam_confidence())
print()

def find_email_sent_days():
    lines = h.split('\n')
    days = {}
    for i in lines:
        if i.startswith('From'):
            day = (i.split(' '))
            if len(day) >= 3:
                day = day[2]
                if day in days:
                    days[day] += 1
                else:
                    days[day] = 1
    return days

print(find_email_sent_days())
print()

def count_message_from_email():
    lines = h.split('\n')
    senders = {}
    for i in lines:
        if i.startswith('From') and len(i.split(' ')) > 2:
            mail = (i.split(' '))[1]
            if mail in senders:
                senders[mail] += 1
            else:
                senders[mail] = 1
    return senders

print(count_message_from_email())
print()

def count_message_from_domain():
    lines = h.split('\n')
    domains = {}
    for i in lines:
        if i.startswith('From') and len(i.split(' ')) > 2:
            mail = (i.split(' '))[1]
            domain = mail.split('@')[1]
            if domain in domains:
                domains[domain] += 1
            else:
                domains[domain] = 1
    return domains

print(count_message_from_domain())
print()
