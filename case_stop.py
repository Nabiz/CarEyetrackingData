import matplotlib.pyplot as plt

# Start Car On Stop
# Hit StopCar


def case_stop(all_data):
    statuses, fixations, events = all_data.statuses, all_data.fixations, all_data.events

    stop_sign_fixation = None
    car_fixation = None

    for fix in fixations:
        if fix["hit_object"] == "signB20" and stop_sign_fixation is None:
            stop_sign_fixation = fix
        if fix["hit_object"] == "StopCar" and car_fixation is None:
            car_fixation = fix

    start_stop_car_event = None
    hit_car_event = None

    for event in events:
        if event["info"] == "Start Car On Stop" and start_stop_car_event is None:
            start_stop_car_event = event
        if event["info"] == "Hit StopCar" and hit_car_event is None:
            hit_car_event = event

    break_status = None
    stop_status = None

    if start_stop_car_event:
        case_statuses = [s for s in statuses if
                         start_stop_car_event["timestamp"] <= s["timestamp"] <= start_stop_car_event["timestamp"] + 10.0]
        for status in case_statuses:
            if status['break_input'] > 0.01 and break_status is None:
                break_status = status
            if status['speed'] < 1 and stop_status is None:
                stop_status = status

    x = 0
    for i in [stop_sign_fixation, car_fixation, start_stop_car_event, hit_car_event, break_status, stop_status]:
        x += 1
        if i:
            print(x, i["timestamp"])
