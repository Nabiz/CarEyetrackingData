from pupil.pupil_src.shared_modules import file_methods as fm


def main(fixation_id):
    for k, v in fixation_data[0][fixation_id].items():
        if k == "timestamp":
            fixation_timestamp = v
        elif k == "duration":
            fixation_duration = v

    aoi = None
    for i in range(len(annotation_data[0])):
        for k, v in annotation_data[0][i].items():
            if fixation_timestamp + fixation_duration/1000 >= annotation_data[0][i]["timestamp"] >= fixation_timestamp:
                if k == "label":
                    aoi = v

    return fixation_timestamp, fixation_duration, aoi


if __name__ == '__main__':
    annotation_data = fm.load_pldata_file("003", "annotation")
    fixation_data = fm.load_pldata_file("003/offline_data", "fixations")
    print(len(fixation_data[0]))
    for i in range(0, len(fixation_data[0])):
        result = main(i)
        print(result)

