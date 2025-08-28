from pupil.pupil_src.shared_modules import file_methods as fm
import matplotlib.pyplot as plt
from os import path


data_path = "data\\Dograjnocka\\2024_06_29\\009"

pupils = fm.load_pldata_file(data_path, "pupil")

confidence_0 = []
confidence_1 = []

for p in pupils[0]:
    if p['topic'] in ("pupil.0.3d", "pupil.1.3d"):
        timestamp = p['timestamp']
        confidence = p['confidence']
        if p['id'] == 0:
            confidence_0.append({'timestamp': timestamp, 'confidence': confidence})
        elif p['id'] == 1:
            confidence_1.append({'timestamp': timestamp, 'confidence': confidence})

time_start = min(confidence_0[0]["timestamp"], confidence_1[0]["timestamp"])
for c in confidence_0:
    c["timestamp"] -= time_start
for c in confidence_1:
    c["timestamp"] -= time_start

# for c in confidence[0]:
#     print(c['confidence'])
# print(len(confidence[0]))

c0_08, c0_06, c0_0, c0_00 = 0, 0, 0, 0
c1_08, c1_06, c1_0, c1_00 = 0, 0, 0, 0
for c in confidence_0:
    con = c["confidence"]
    if con >= 0.8:
        c0_08 += 1
    elif con >= 0.6:
        c0_06 += 1
    elif con > 0.0:
        c0_0 += 1
    elif con == 0.0:
        c0_00 += 1

for c in confidence_1:
    con = c["confidence"]
    if con >= 0.8:
        c1_08 += 1
    elif con >= 0.6:
        c1_06 += 1
    elif con > 0.0:
        c1_0 += 1
    elif con == 0.0:
        c1_00 += 1

print(c0_08, ',', c0_06, ',', c0_0, ',', c0_00)
print(c1_08, ',', c1_06, ',', c1_0, ',', c1_00)


# Extract values
timestamps0 = [d['timestamp'] for d in confidence_0]
confidences0 = [d['confidence'] for d in confidence_0]

timestamps1 = [d['timestamp'] for d in confidence_1]
confidences1 = [d['confidence'] for d in confidence_1]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), sharey=True)

# Plot
# plt.figure(figsize=(10, 5))
ax1.plot(timestamps0, confidences0, marker='o', markersize=1, linestyle='None', color='b', linewidth=0.1)
ax1.axhline(y=0.8, color='r', linestyle='--', linewidth=1.5, label='Threshold 0.8')
ax1.axhline(y=0.6, color='g', linestyle='--', linewidth=1.5, label='Threshold 0.6')
ax1.set_title('Confidence over Time - Left Eye')
ax1.set_xlabel('Timestamp (s)')
ax1.set_ylabel('Confidence')

# Plot
# plt.figure(figsize=(10, 5))
ax2.plot(timestamps1, confidences1, marker='o', markersize=1, linestyle='None', color='b', linewidth=0.1)
ax2.axhline(y=0.8, color='r', linestyle='--', linewidth=1.5, label='Threshold 0.8')
ax2.axhline(y=0.6, color='g', linestyle='--', linewidth=1.5, label='Threshold 0.6')
ax2.set_title('Confidence over Time - Right Eye')
ax2.set_xlabel('Timestamp (s)')
ax2.set_ylabel('Confidence')


plt.grid(True)
plt.tight_layout()
plt.show()

