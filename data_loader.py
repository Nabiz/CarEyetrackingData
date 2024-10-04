from pupil.pupil_src.shared_modules import file_methods as fm
from os import path


def load_data(data_path):
    offline_data_path = path.join(data_path, "offline_data")
    annotation_data = fm.load_pldata_file(data_path, "annotation")
    fixation_data = fm.load_pldata_file(offline_data_path, "fixations")
    return fixation_data, annotation_data


def get_parsed_fixation_data(fixation_data):
    fixations = []
    keys = ["id", "timestamp", "duration"]
    for fixation in fixation_data[0]:
        fixations.append({k: v for (k, v) in fixation.items() if k in keys})
    return fixations


def get_parsed_car_status_data(annotation_data):
    car_statuses = []
    keys = ["timestamp", "speed", "pos_x", "pos_y", "gas_input", "break_input", "wheel_input"]
    for annotation in annotation_data[0]:
        if annotation["label"] == "car_status":
            car_statuses.append({k: v for (k, v) in annotation.items() if k in keys})
    return car_statuses


def get_parsed_event_data(annotation_data):
    events = []
    keys = ["timestamp", "info"]
    for annotation in annotation_data[0]:
        if annotation["label"] == "event":
            events.append({k: v for (k, v) in annotation.items() if k in keys})
    return events


def get_parsed_hit_object_data(annotation_data):
    hit_objects = []
    keys = ["timestamp", "hit_object", "distance"]
    for annotation in annotation_data[0]:
        if annotation["label"] == "hit_object":
            hit_objects.append({k: v for (k, v) in annotation.items() if k in keys})
    return hit_objects

