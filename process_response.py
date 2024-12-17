def separate(text):
    parts = text.split(":")
    initial_text = 't'+parts[0].strip()[1:]
    jobs_list = ''
    temp = parts[1].strip().split("^")[1:]
    for i in range(len(temp)):
        if(i == len(temp)-1):
            jobs_list += temp[i]
            break
        jobs_list += temp[i][:-1]+', '
    return initial_text, jobs_list