import xml.etree.ElementTree as ET

search = input(str("What data would you like to retrieve?"))
all_final_times = []

path = 'PitOf100Trials.lss'

with open(path, 'rb') as f:
        binary_data = f.read()

root = ET.fromstring(binary_data)

for run in root.findall('AttemptHistory/Attempt'):
    date = run.get('started')

    final_time = run.find('RealTime')

    if final_time is not None:
        all_final_times.append({
            "date": date, 
            "time": final_time.text
        })

for run in all_final_times:

    print(f"{run['date']}, {run['time']}")
