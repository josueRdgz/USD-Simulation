import random
import statistics

# 7 days
last_values_mean=[173,175,177,180,182,183,185]
last_values_median=[173,175,177,180,182,183,185]
last_values_mode=[173,175,177,180,182,183,185]
day=0

# Random reference to increase or decrease values 
states=[-1,0,1]

# k is index of fake value
def Simulate_Mean(k):
    value_random = random.choice(states)
    if day%5==0:
        last_values_mean[0]+=k
    if day%6==0:
        last_values_mean[0]-=k
    if value_random == -1:
        last_values_mean[day%7]= int(statistics.mean(last_values_mean) - 5)
    elif value_random == 1:
        last_values_mean[day%7]= int(statistics.mean(last_values_mean) + 5)
    else:
        last_values_mean[day%7]= int(statistics.mean(last_values_mean))
    return last_values_mean[day%7]

def Simulate_Median(k):
    value_random = random.choice(states)
    if day%5==0:
            last_values_median[0]+=k
    if day%6==0:
        last_values_median[0]-=k
    if value_random == -1:
        last_values_median[day%7]= int(statistics.median(last_values_median)-5)
    elif value_random == 1:
        last_values_median[day%7]= int(statistics.median(last_values_median)+5)
    else: 
        last_values_median[day%7]= int(statistics.median(last_values_median))
    return last_values_median[day%7]

def Simulate_Mode(k):
    value_random = random.choice(states)
    if day%5==0:
            last_values_mode[0]+=k
    if day%6==0:
        last_values_mode[0]-=k
    if value_random == -1:
        last_values_mode[day%7]= int(statistics.mode(last_values_mode)-5)
    elif value_random == 1:
        last_values_mode[day%7]= int(statistics.mode(last_values_mode)+5)
    else:
        last_values_mode[day%7]= int(statistics.mode(last_values_mode))
    
    return last_values_mode[day%7]

#Simulation for 100 days
while day < 100:
     print("Mean: ",Simulate_Mean(5))
     print("Median: ",Simulate_Median(20))
     print("Mode: ",Simulate_Mode(10))
     day+=1
