#!/usr/bin/python
#   @author Brain Fox and Greg Walsh
#  ______      _              ______                          _   _____                  _    _       _     _     
#    ___ \    (_)             |  ___|                        | | |  __ \                | |  | |     | |   | |    
#  | |_/ /_ __ _  __ _ _ __   | |_ _____  __   __ _ _ __   __| | | |  \/_ __ ___  __ _  | |  | | __ _| |___| |__  
#  | ___ \ '__| |/ _` | '_ \  |  _/ _ \ \/ /  / _` | '_ \ / _` | | | __| '__/ _ \/ _` | | |/\| |/ _` | / __| '_ \ 
#  | |_/ / |  | | (_| | | | | | || (_) >  <  | (_| | | | | (_| | | |_\ \ | |  __/ (_| | \  /\  / (_| | \__ \ | | |
#  \____/|_|  |_|\__,_|_| |_| \_| \___/_/\_\  \__,_|_| |_|\__,_|  \____/_|  \___|\__, |  \/  \/ \__,_|_|___/_| |_|
#                                                                                 __/ |                           
#                                                                                |___/                             
#Local Search with Simulated Annealing

import math
import sys
from random import randrange
def parse_tsp_data(path):
    '''
    returns list of cities as a 3-tuple in the form (city id,x,y) 
    '''
    tsp_data = open(path)
    for line in tsp_data:
        if line.split()[0]  == "NODE_COORD_SECTION":
            break
    
    city_list = list()
    for line in tsp_data:
        if line == "EOF":
            break
        n,x,y = line.split()
        city_list.append((n,x,y))

    tsp_data.close()
    return city_list

def euc_distance(city1,city2):
    '''
    calculates euclidean distance 
    note: we do not round this value so we're using the exact distance
    '''
    n,x1,y1 = city1
    n,x2,y2 = city2
    x1,x2,y1,y2 = [float(n) for n in [x1,x2,y1,y2]]

    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def generate_random_tour(city_list):
    '''
    implementation of fisher-yates shuffle
    '''
    perm = list(city_list)
    for i in range(len(city_list)-1):
        j = randrange(len(city_list)-i) + i
        perm[i],perm[j] = perm[j],perm[i]
    return perm


def get_tour_distance(tour_list):
    total_dist = 0
    last_city = tour_list[-1]
    for city in tour_list:
        total_dist = total_dist + euc_distance(city,last_city)
        last_city = city
    return total_dist


if __name__=="__main__":
    if(len(sys.argv)<2):
        exit()
    city_list = parse_tsp_data(sys.argv[1])
    print(euc_distance(city_list[0],city_list[1]))
    print(get_tour_distance(city_list))
    print(get_tour_distance(generate_random_tour(city_list)))
    

