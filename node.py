import random
import numpy as np
from collections import deque
import matplotlib.pyplot as plt



class GraphGenerator:
    
    def __init__(self, total_nodes: int = 30):
        
        
        self.nodes_list = self.generate_nodes(total_nodes)
        
        self.display_nodes()
    
        

    
    
    def generate_nodes(self, total_nodes):
        
        initial_node = {
            "node_ID": 0,
            "position": (0, 0) }
        
        
        nodes_list = [initial_node]
        
        queue = deque([initial_node])
        
        
        expanded = set()
        
        current_layer = 0
        
        self.current_ID = 0
        
        
        while len(nodes_list) < total_nodes:
            
            current_node = queue.popleft()
            
            
            expanded.add(current_node["node_ID"])
            
            
            self.generate_new_nodes(current_node, nodes_list, queue, current_layer)
            
                
                
            current_layer += 1
            
            
        return nodes_list
        
    
    
        
        
    def generate_new_nodes(self, current_node: dict, nodes_list, queue, current_layer: int) -> None:
        
        
        current_node_ID = current_node["node_ID"]
        current_position = current_node["position"]
        
        
        new_nodes_list = list()
        
        new_nodes_amount = self.get_number_of_nodes_to_generate(current_layer)   
        
        
        angle = -20              # degrees
        
        
        for i in range(new_nodes_amount):
            
            
            angle = angle + self.get_random_angle(current_layer)

            new_position = self.get_position_of_new_node(current_position, current_layer, angle)
            
            
            new_node = {
                "node_ID": self.current_ID + (i + 1),
                "position": new_position }
            
            self.current_ID += 1
            
            
            new_nodes_list.append(new_node)
            
            queue.append(new_node)
        
        
        nodes_list.extend(new_nodes_list)
        
        
    
    
    def get_number_of_nodes_to_generate(self, current_layer: int) -> int:
        
        if current_layer == 0:
            return random.randint(3, 6)
        
        
        return random.randint(1, 4)
    
        
    
    def get_random_angle(self, current_layer: int) -> float:
        
        if current_layer == 0:
            return random.uniform(0, 360)
        
        
        return random.uniform(-30, 45)
    
    
    def get_change_in_position(self, current_angle: float,  new_angle: float, distance: float) -> tuple:
        
        delta_x = distance * np.cos(np.radians(new_angle + current_angle)) 
          
        delta_y = distance * np.sin(np.radians(new_angle + current_angle))
        
        return (delta_x, delta_y)
    
    
    
    
    def get_angle_of_node(self, node_position: tuple) -> float:
        
        x, y = node_position
        
        return np.degrees(np.arctan2(y, x))
    
    
    def get_position_of_new_node(self, current_position: tuple, current_layer: int, angle: float) -> tuple:
        
            
        distance = random.uniform(1, 3)
        
        current_angle = self.get_angle_of_node(current_position)
        
        
        delta_x, delta_y = self.get_change_in_position(current_angle, angle, distance)
        
        new_x = current_position[0] + delta_x
        new_y = current_position[1] + delta_y


        new_position = (new_x, new_y)

        return new_position
    
    
    
    def display_nodes(self):
    
        print("Nodes generated: \n")
        
        for node in self.nodes_list:
            print(f"Node ID: {node['node_ID']}, Position: {round(node['position'][0], 2)}, {round(node['position'][1], 2)}")
            
        x_coords = [node['position'][0] for node in self.nodes_list]
        y_coords = [node['position'][1] for node in self.nodes_list]

        plt.scatter(x_coords, y_coords)

        for i, node in enumerate(self.nodes_list):
            plt.text(node['position'][0], node['position'][1], str(node['node_ID']))

        plt.show()




GraphGenerator()