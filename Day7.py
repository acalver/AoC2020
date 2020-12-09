import re
import itertools
import pandas as pd

bag_csv = pd.read_csv('./data/Day7_bags.csv', header = None)
bag_input = bag_csv[0].values

bag_graph = dict()
for bag in bag_input:
    test = re.sub('contain', '', bag)
    test = re.sub('[.,]', '', test)
    test = re.split('bags?', test)
    outer_bag = test[0].strip()
    inner_bags = []

    for inner in test[1:]:
        
        inner = inner.strip()
        
        if inner[:2] == 'no':
            break
        elif len(inner) > 0:
            #num_of_bags = int(inner[0])
            #*num_of_bags
            inner_bags.append([inner[2:]])
            
    inner_bags = list(itertools.chain.from_iterable(inner_bags))
    bag_graph[outer_bag] = inner_bags

def bagRecursion(start, graph = bag_graph, path = []):
    path = path + [start]
    #print(path)
    if 'shiny gold' in path:
        return 1
    
    for node in graph[start]:
        
        if node not in path and len(node) > 0:
            newpath = bagRecursion(node, path = path)
            
            if newpath:
                return newpath
    
    return 0

count = 0
for keys in bag_graph.keys():
    
    if keys != 'shiny gold':
        count += bagRecursion(keys)

    

def shinyGoldRecursion(start = 'shiny gold', graph = bag_graph, path = []):
    path = path + [start]
    
    for node in graph[start]:
        print(node)
        if node not in path and len(node) > 0:
            newpath = bagRecursion(start = node, path = path)
            
            if newpath:
                return newpath
    
    return path


shinyGoldRecursion()