import data_loader as dl
import utils
import matplotlib.pyplot as plt

"""Load Data from Pupil files"""
fix_data, ann_data = dl.load_data("data\\Dograjnocka\\2024_06_28\\004")
fixations = dl.get_parsed_fixation_data(fix_data)
statuses = dl.get_parsed_car_status_data(ann_data)
events = dl.get_parsed_event_data(ann_data)
hit_objects = dl.get_parsed_hit_object_data(ann_data)

"""Setup time and align fixations to objects"""
utils.reset_time(fixations, statuses, events, hit_objects)
utils.add_hit_objects_to_fixations(fixations, hit_objects)


# """Print all fixations with objects"""
# for fix in fixations:
#     if fix["hit_object"] != "None":
#         print(fix["id"])
#         print(fix["timestamp"])
#         print(fix["hit_object"])

plt.plot([status["timestamp"] for status in statuses], [status["speed"] for status in statuses])
plt.plot([status["timestamp"] for status in statuses], [100*status["break_input"] for status in statuses], color="red")

jenny_timestamps = []
jenny_distances = []

for fix in fixations:
    if fix["hit_object"] == "Jenny":
        plt.axvline(fix["timestamp"], color='g')
        jenny_timestamps.append(fix["timestamp"])
        jenny_distances.append(fix["distance"])

spawn_pedestrian_timestamps = None
for event in events:
    print(event)
    if event["info"] == "Spawn Jenny":
        plt.axvline(event["timestamp"], color="orange")
        spawn_pedestrian_timestamps = event["timestamp"]

break_timestamp = None
for status in statuses:
    if spawn_pedestrian_timestamps <= status["timestamp"] <= spawn_pedestrian_timestamps + 10.0:
        if status["break_input"] > 0.05:
            break_timestamp = status["timestamp"]
            break

print("Od spawnu do Jenny", jenny_timestamps[0]-spawn_pedestrian_timestamps, jenny_distances[0], "metry")
print("Od spwanu do hamulca", break_timestamp-spawn_pedestrian_timestamps)
print("Od jenny do hamulca", break_timestamp-jenny_timestamps[0])

plt.show()