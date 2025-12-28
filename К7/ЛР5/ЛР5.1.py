def find_speed_pair(speeds, target_sum):
    left = 0                  
    right = len(speeds) - 1  
    while left < right:
        current_sum = speeds[left] + speeds[right]
        if current_sum == target_sum:
            return speeds[left], speeds[right]
        elif current_sum < target_sum:
            left += 1        
        else:
            right -= 1       
    return None

speeds = [20, 30, 40, 50, 60, 70]
target = 90
result = find_speed_pair(speeds, target)
if result:
    print("Найдена пара скоростей:", result)
else:
    print("Пара с такой суммой не найдена")
