def distances_between_repeats(s):
    last_seen = {}      
    distances = []       

    for i, ch in enumerate(s):
        if ch in last_seen:                  
            distances.append(i - last_seen[ch])
        last_seen[ch] = i                  

    return distances
print(distances_between_repeats("abcaab"))
