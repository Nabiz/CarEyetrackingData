from pupil.pupil_src.shared_modules import file_methods as fm

annotation_data = fm.load_pldata_file("000", "annotation")
print(annotation_data[0])
for annotation in annotation_data[0]:
    if annotation["label"] == 'CarStatus':
        print(annotation)