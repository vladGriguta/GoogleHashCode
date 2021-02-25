# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

class car:
    def __init__(self, itinerary):
        self.itinerary = itinerary
        self.freeze = 0
    def transit_current_intersection(self,T):
        intersection_id = streets[self.itinerary[0]][1]
        incoming_street = self.itinerary[0]
        if intersections[intersection_id].is_green(incoming_street):
            self.itinerary.pop(0)
            outgoing_street = self.itinerary[0]
            self.freeze += 1 + streets[outgoing_street][2]
    def make_step(self, T):
        if self.freeze > 0:
            self.freeze -= 1
        elif len(self.itinerary)>1:
            self.transit_current_intersection(T)
        else:
            pass
    def has_transitioned(self,):
        if self.freeze == 0 and len(self.itinerary)==1:
            return True
        return False


class StreetNode:
    def __init__(self, assigned_time, street_name):
        self.assigned_time = assigned_time
        self.remaining_time = assigned_time
        self.street_name = street_name
        self.next = None
        
    def reset_time(self,):
        self.remaining_time = self.assigned_time
        
    def make_step(self,):
        if self.remaining_time == 0:
            self = self.next
            self.reset_time()
        else:
            self.remaining_time -= 1


class intersection:
    def __init__(self, idx):
        self.idx = idx
        self.streets = []
        self.initialized = False
    
    def add_direction(self,street_name):
        self.streets.append(street_name)
        
    def build_light_cycle(self, mapping=None):
        if not mapping:
            mapping = [(el,1) for el in self.streets]
        
        self.mapping = mapping
        init_node = StreetNode(mapping[0][1], mapping[0][0])
        node = init_node
        for i in range(len(mapping)):
            node.next = StreetNode(mapping[i][1], mapping[i][0])
            node = node.next
        node.next = init_node
        self.street_node = init_node
        
    def return_streets(self,):
        return self.streets
    
    def is_green(self, direction_street):
        return self.street_node.street_name == direction_street
    
    def make_step(self,):
        self.street_node.make_step()
    
    def to_string(self,):
        return '{}\n{}\n'.format(self.idx, len(self.mapping)) + '\n'.join([
            el[0]+' '+str(el[1]) for el in self.mapping])
        
def run_simulation(cars):
    for T in range(D):
        all_cars_transitioned = True
        for car in cars:
            car.make_step(T)
            if not car.has_transitioned():
                all_cars_transitioned = False
        
        if all_cars_transitioned:
            break
        
        for idx in intersections:
            intersections[idx].make_step()

if __name__ == '__main__':
    files = ['a','b','c','d','e','f']
    #for file in files:
    
    file = 'a'
    max_num = 3
    streets = {}
    intersections = {}
    cars = []
    
    with open('{}.txt'.format(file)) as f:
        header = f.readline()
        D, I, S, V, F = [int(el) for el in header.split(' ')]
        
        for _ in range(S):
            line_elems = f.readline().split(' ')
            intersection_start_idx = int(line_elems[0])
            intersection_end_idx = int(line_elems[1])
            street_name = line_elems[2]
            duration = int(line_elems[3])
            streets[street_name] = (intersection_start_idx, intersection_end_idx, duration)
            
            # add intersection
            if intersection_end_idx not in intersections:
                intersections[intersection_end_idx] = intersection(intersection_end_idx)
            intersections[intersection_end_idx].add_direction(street_name)
    
        for _ in range(V):
            line_elems = f.readline().split(' ')
            num_streets_to_travel = int(line_elems[0])
            cars.append(car(line_elems[1:]))
    
    ## initialise intersections
    for idx in intersections:
        sample_mapping = [(street, 1) for street in intersections[idx].streets]
        intersections[idx].build_light_cycle(sample_mapping)

    run_simulation(cars)
    
    num_cars_transitioned = 0
    for car in cars:
        if car.has_transitioned():
            num_cars_transitioned += 1
    print(num_cars_transitioned)

    """
    with open('{}_out.txt'.format(file),'w') as f:
        f.write('{}\n'.format(len(intersections)))
        for idx in intersections:
            f.write(intersections[idx].to_string()+'\n')
    """