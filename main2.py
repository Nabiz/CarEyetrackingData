import data_loader as dl
import matplotlib.pyplot as plt
import numpy as np

fix_data, ann_data = dl.load_data("data\\000")

fixations = dl.get_parsed_fixation_data(fix_data)

statuses = dl.get_parsed_car_status_data(ann_data)

events = dl.get_parsed_event_data(ann_data)

hit_objects = dl.get_parsed_hit_object_data(ann_data)


for i in range(len(fixations)):
    fix = fixations[i]
    object_hit_count_dict = {}

    fix["hit_object"] = "None"
    for hit_object in hit_objects:
        if fix["timestamp"] <= hit_object["timestamp"] <= fix["timestamp"] + fix["duration"]/1000:
            if hit_object["hit_object"] in object_hit_count_dict:
                object_hit_count_dict[hit_object["hit_object"]] += 1
            else:
                object_hit_count_dict[hit_object["hit_object"]] = 1
    if len(object_hit_count_dict) > 0:
        fix["hit_object"] = max(object_hit_count_dict, key=object_hit_count_dict.get)

for i in range(len(fixations)):
    fix = fixations[i]
    print(fix["id"], fix["timestamp"], fix["duration"], fix["hit_object"])




