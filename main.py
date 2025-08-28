import data_loader as dl
import utils
from case_stop import case_stop
from case_jenny import case_jenny
from case_lights import case_lights
from case_brian import case_brian

"""Load Data from Pupil files"""
case_output = []
for i in range(1, 20):
    fix_data, ann_data = dl.load_data("data\\FinalData\\"+str(i))

    fixations = dl.get_parsed_fixation_data(fix_data)
    statuses = dl.get_parsed_car_status_data(ann_data)
    events = dl.get_parsed_event_data(ann_data)
    hit_objects = dl.get_parsed_hit_object_data(ann_data)

    """Setup time and align fixations to objects"""
    utils.reset_time(fixations, statuses, events, hit_objects)
    utils.add_hit_objects_to_fixations(fixations, hit_objects)
    all_data = utils.AllData(statuses=statuses, fixations=fixations, events=events)

    # print("\n")
    # case_stop(all_data)
    # case_output.append(case_lights(all_data))
    # case_output.append(case_jenny(all_data))
    # print("\n")
    #case_output.append(case_brian(all_data))

    case_output.append(statuses[-1]["timestamp"])

for c in case_output:
#     print((str(c[0])+";"+str(c[1])+";"+str(c[2])).replace(".", ","))
    print(str(c).replace(".", ","))
