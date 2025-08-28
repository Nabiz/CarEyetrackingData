def reset_time(fixations, statuses, events, hit_objects):
    start_time = min(fixations[0]["timestamp"], statuses[0]["timestamp"], events[0]["timestamp"],
                     hit_objects[0]["timestamp"])

    for fixation in fixations:
        fixation["timestamp"] -= start_time
    for status in statuses:
        status["timestamp"] -= start_time
    for event in events:
        event["timestamp"] -= start_time
    for hit_object in hit_objects:
        hit_object["timestamp"] -= start_time


def add_hit_objects_to_fixations(fixations, hit_objects):
    for i in range(len(fixations)):
        fix = fixations[i]
        object_hit_count_dict = {}

        fix["hit_object"] = "None"
        for hit_object in hit_objects:
            if fix["timestamp"] <= hit_object["timestamp"] <= fix["timestamp"] + fix["duration"] / 1000:
                if hit_object["hit_object"] in object_hit_count_dict:
                    object_hit_count_dict[hit_object["hit_object"]] += 1
                else:
                    object_hit_count_dict[hit_object["hit_object"]] = 1
        if len(object_hit_count_dict) > 0:
            fix["hit_object"] = max(object_hit_count_dict, key=object_hit_count_dict.get)
            for hit_object in hit_objects:
                if hit_object["hit_object"] == fix["hit_object"]:
                    fix["distance"] = hit_object["distance"]
                    break


class AllData:
    def __init__(self, statuses, fixations, events):
        self.statuses = statuses
        self.fixations = fixations
        self.events = events
