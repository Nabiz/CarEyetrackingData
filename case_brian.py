import matplotlib.pyplot as plt
import numpy as np


def case_brian(all_data):
    statuses, fixations, events = all_data.statuses, all_data.fixations, all_data.events

    jenny_timestamps = []
    jenny_distances = []

    for fix in fixations:
        if fix["hit_object"] == "Brian":
            jenny_timestamps.append(fix["timestamp"])
            jenny_distances.append(fix["distance"])

    spawn_pedestrian_timestamp = None
    for event in events:
        if event["info"] == "Spawn Brian" and spawn_pedestrian_timestamp is None:
            spawn_pedestrian_timestamp = event["timestamp"]

    break_timestamp = None
    for status in statuses:
        if spawn_pedestrian_timestamp <= status["timestamp"] <= spawn_pedestrian_timestamp + 10.0:
            if status["break_input"] > 0.1:
                break_timestamp = status["timestamp"]
                break

    jenny_hit_event = None
    for event in events:
        if event["info"] == "Hit Brian" and jenny_hit_event is None:
            jenny_hit_event = event

    if spawn_pedestrian_timestamp:
        case_statuses = [s for s in statuses if
                         spawn_pedestrian_timestamp - 4.0 <= s["timestamp"] <= spawn_pedestrian_timestamp + 8.0]

        statuses = case_statuses

    # Example data
    time = [status["timestamp"] for status in statuses]
    brake_input = [status["break_input"] for status in statuses]
    speed = [status["speed"] for status in statuses]

    # Create figure and left axis
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
    # ax1.axvline(x=spawn_pedestrian_timestamp, color='green', linestyle='-', linewidth=1.5, alpha=0.7)
    # if jenny_hit_event:
    #     ax1.axvline(x=jenny_hit_event["timestamp"], color='yellow', linestyle='-', linewidth=1.5, alpha=0.7)
    #
    # for jt in jenny_timestamps:
    #     if jt < spawn_pedestrian_timestamp + 10:
    #         ax1.axvline(x=jt, color='grey', linestyle=':', linewidth=1.5, alpha=0.7)
    #
    # # Title and layout
    # plt.title("Brake Input and Speed Over Time")
    # fig.tight_layout()
    # plt.grid(True)
    # plt.show()


    a, b, c = '-', '-', '-'
    if spawn_pedestrian_timestamp:
        a = spawn_pedestrian_timestamp

    for jt in jenny_timestamps:
        if jt > spawn_pedestrian_timestamp:
            b = jt
            break

    break_timestamp = None
    for status in statuses:
        if spawn_pedestrian_timestamp <= status["timestamp"] <= spawn_pedestrian_timestamp + 6.0:
            if status["break_input"] > 0.02:
                break_timestamp = status["timestamp"]
                break

    if break_timestamp:
        c = break_timestamp

    return a, b, c
