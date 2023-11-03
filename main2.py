import data_loader as dl
import matplotlib.pyplot as plt
import numpy as np

fix_data, ann_data = dl.load_data("data\\002")

fixations = dl.get_parsed_fixation_data(fix_data)

statuses = dl.get_parsed_car_status_data(ann_data)

events = dl.get_parsed_event_data(ann_data)

hit_objects = dl.get_parsed_hit_object_data(ann_data)


for fixation in fixations:
    #print(fixation["timestamp"], fixation["duration"])
    for hit_object in hit_objects:
        if fixation["timestamp"] <= hit_object["timestamp"] <= fixation["timestamp"] + fixation["duration"]/1000:
            if(hit_object["hit_object"] == 'Jenny'):
                print(hit_object)




