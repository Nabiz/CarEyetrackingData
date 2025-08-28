import matplotlib.pyplot as plt
import numpy as np


def case_lights(all_data):
    statuses, fixations, events = all_data.statuses, all_data.fixations, all_data.events

    traffic_light_fixation = None
    traffic_light_fixations = []

    for fix in fixations:
        if fix["hit_object"] == "TrafficLight":
            traffic_light_fixations.append(fix)
            if traffic_light_fixation is None:
                traffic_light_fixation = fix


    light_collider_event = None
    warn_light_event = None
    stop_light_event = None
    ready_light_event = None
    go_light_event = None

    for event in events:
        if event["info"] == "Light Collider" and light_collider_event is None:
            light_collider_event = event
        if event["info"] == "Light Warn" and warn_light_event is None:
            warn_light_event = event
        if event["info"] == "Light Stop" and stop_light_event is None:
            stop_light_event = event
        if event["info"] == "Light Ready" and ready_light_event is None:
            ready_light_event = event
        if event["info"] == "Light Go" and go_light_event is None:
            go_light_event = event

    break_status = None
    stop_status = None

    if light_collider_event:
        case_statuses = [s for s in statuses if
                         light_collider_event["timestamp"] - 5.0 <= s["timestamp"] <= go_light_event["timestamp"] + 5.0]
        for status in case_statuses:
            if status['break_input'] > 0.01 and break_status is None:
                break_status = status
            if status['speed'] < 1 and stop_status is None:
                stop_status = status

        statuses = case_statuses

    # Example data
    time = [status["timestamp"] for status in statuses]
    brake_input = [status["break_input"] for status in statuses]
    speed = [status["speed"] for status in statuses]

    # # Create figure and left axis
    # fig, ax1 = plt.subplots(figsize=(10, 5))
    #
    # # Left Y-axis: Brake input
    # ax1.set_xlabel("Time (s)")
    # ax1.set_ylabel("Brake Input", color='tab:red')
    # ax1.plot(time, brake_input, color='tab:red', label='Brake Input')
    # ax1.tick_params(axis='y', labelcolor='tab:red')
    # ax1.set_xticks(np.arange(int(time[0]), int(time[-1]+1), 1.0))
    #
    # # Right Y-axis: Speed
    # ax2 = ax1.twinx()
    # ax2.set_ylabel("Speed (km/h)", color='tab:blue')
    # ax2.plot(time, speed, color='tab:blue', label='Speed')
    # ax2.tick_params(axis='y', labelcolor='tab:blue')
    #
    # # Event timestamps
    # #ax1.axvline(x=light_collider_event["timestamp"], color='gray', linestyle='-', linewidth=1.5, alpha=0.7)
    # ax1.axvline(x=warn_light_event["timestamp"], color='yellow', linestyle='-', linewidth=1.5, alpha=0.7)
    # ax1.axvline(x=stop_light_event["timestamp"], color='red', linestyle='-', linewidth=1.5, alpha=0.7)
    # ax1.axvline(x=ready_light_event["timestamp"], color='yellow', linestyle='-', linewidth=1.5, alpha=0.7)
    # ax1.axvline(x=go_light_event["timestamp"], color='green', linestyle='-', linewidth=1.5, alpha=0.7)
    #
    # for tlf in traffic_light_fixations:
    #     if tlf["timestamp"] < go_light_event["timestamp"]:
    #         ax1.axvline(x=tlf["timestamp"], color='grey', linestyle=':', linewidth=1.5, alpha=0.7)
    #
    # # Title and layout
    # plt.title("Brake Input and Speed Over Time")
    # fig.tight_layout()
    # plt.grid(True)
    # plt.show()

    a, b, c = '-', '-', '-'
    if warn_light_event:
        a = warn_light_event["timestamp"]

    for tlf in traffic_light_fixations:
        if tlf["timestamp"] > warn_light_event["timestamp"]:
            b = tlf["timestamp"]
            break

    break_timestamp = None
    for status in statuses:
        if warn_light_event["timestamp"] <= status["timestamp"] <= warn_light_event["timestamp"] + 10.0:
            if status["break_input"] > 0.02:
                break_timestamp = status["timestamp"]
                break

    if break_timestamp:
        c = break_timestamp

    return a,b,c
