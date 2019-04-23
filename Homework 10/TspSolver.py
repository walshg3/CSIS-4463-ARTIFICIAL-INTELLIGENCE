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

def generate_random_neighbor(city_list):

    neighbor = list(city_list)
    j = randrange(len(neighbor))
    i = j
    while i == j :
        i = randrange(len(neighbor))

    neighbor[i],neighbor[j] = neighbor[j],neighbor[i]

    return neighbor

def get_tour_distance(tour_list):
    total_dist = 0
    last_city = tour_list[-1]
    for city in tour_list:
        total_dist = total_dist + euc_distance(city,last_city)
        last_city = city
    return total_dist

class tour_neighbors:

    def __init__(self,tour):
        self.tour = tour
        

    def __iter__(self):
        self.left = 0
        self.right = 1
        return self

    def __next__(self):
        if (self.left == len(self.tour)-1):
            raise StopIteration
        neighbor = list(self.tour)
        neighbor[self.left],neighbor[self.right] = neighbor[self.right],neighbor[self.left]
        if self.right < len(self.tour)-1:
            self.right = self.right +1
        else:
            self.left = self.left + 1
            self.right = self.left + 1

        return neighbor




def search(city_list):
    tour = generate_random_tour(city_list)
    tour_dist = get_tour_distance(tour)
    count = 0
    #results were considerably bigger with 10x and slightly smaller with 1000x
    lowest = math.inf
    for i in range(100):
        while(count<5000):
            count = count+1
            neighbor = generate_random_neighbor(tour)
            neighbor_dist = get_tour_distance(neighbor) 
            if(neighbor_dist < tour_dist):
                tour = neighbor
                tour_dist = neighbor_dist
                count = 0
        print(tour_dist)
        if tour_dist < lowest:
            lowest = tour_dist

    '''
    while(True):
        for neighbor in tour_neighbors(tour):
            neighbor_dist = get_tour_distance(neighbor) 
            if (neighbor_dist < tour_dist):
                print(neighbor_dist)
                tour = neighbor
                tour_dist = neighbor_dist
                break
        else:
            break
    '''

    return tour


if __name__=="__main__":
    if(len(sys.argv)<2):
        exit()
    city_list = parse_tsp_data(sys.argv[1])
    #print(euc_distance(city_list[0],city_list[1]))
    #print(get_tour_distance(city_list))
    #print(get_tour_distance(generate_random_tour(city_list)))
    
    print(get_tour_distance(search(city_list)))

