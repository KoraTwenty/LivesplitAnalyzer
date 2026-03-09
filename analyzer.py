import xml.etree.ElementTree as ET
import statistics
import scipy.stats
import os
import sys

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(script_dir)

print("Current directory:", os.getcwd())
path = str(input("File: "))

prompt1 = input(str("What data would you like to retrieve? "))
all_final_times = []
all_split_times = []

def LSStoSeconds(x):
    h, m, s = x.split(":")
    return float(h)*3600 + float(m)*60 + float(s)

with open(path, 'rb') as f:
    binary_data = f.read()

root = ET.fromstring(binary_data)

if prompt1 == "c" or prompt1 == "chrono" or prompt1 == "chronological":
    prompt2 = input(str("What split would you like to search: "))
    if prompt2 == "run" or prompt2 == "*" or prompt2 == "all":
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
    else:
        for split in root.findall('Segments/Segment'):
            name = split.find('Name')
            if name is not None and name.text.strip() == prompt2.strip():
                print(name.text)
                split_times = split.findall('SegmentHistory/Time/RealTime')
                
                for split_time in split_times:
                    if split_time is not None:
                        all_split_times.append({
                            "time": split_time.text
                        })
            
        for split in all_split_times:
            print(f"{split['time']}")

elif prompt1 == "r" or prompt1 == "rank":
    prompt2 = input(str("What split would you like to search: "))
    if prompt2 == "run" or prompt2 == "*" or prompt2 == "all":
        for run in root.findall('AttemptHistory/Attempt'):
            date = run.get('started')

            final_time = run.find('RealTime')

            if final_time is not None:
                all_final_times.append({
                    "date": date, 
                    "time": final_time.text,
                    "seconds": LSStoSeconds(final_time.text)
                })

        all_final_times.sort(key=lambda x: x["seconds"])
        
        for run in all_final_times:
            print(f"{all_final_times.index(run) + 1}. {run['date']}, {run['time']}")
    
    else:
        for split in root.findall('Segments/Segment'):
            name = split.find('Name')
            if name is not None and name.text.strip() == prompt2.strip():
                print(name.text)
                split_times = split.findall('SegmentHistory/Time/RealTime')
                
                for split_time in split_times:
                    if split_time is not None:
                        all_split_times.append({
                            "time": split_time.text,
                            "seconds": LSStoSeconds(split_time.text)
                        })

        all_split_times.sort(key=lambda x: x["seconds"])
            
        for split in all_split_times:
            print(f"{all_split_times.index(split) + 1}. {split['time']}")

elif prompt1 == "p" or prompt1 == "prob" or prompt1 == "probability" or prompt1 == "s" or prompt1 == "stat" or prompt1 == "stats" or prompt1 == "statistics":
    prompt2 = input(str("What split would you like to search: "))
    if prompt2 == "run" or prompt2 == "*" or prompt2 == "all":
        for run in root.findall('AttemptHistory/Attempt'):
            date = run.get('started')

            final_time = run.find('RealTime')

            if final_time is not None:
                all_final_times.append({
                    "date": date, 
                    "time": final_time.text,
                    "seconds": LSStoSeconds(final_time.text)
                })

        all_final_times.sort(key=lambda x: x["seconds"])

        seconds_list = [run["seconds"] for run in all_final_times]
       
        for run in all_final_times:
            print(f"{run['date']}, {run['time']}, {100 * (scipy.stats.norm.cdf(run['seconds'], statistics.mean(seconds_list), statistics.stdev(seconds_list))):.3f}%")

        print(f"Mean: {statistics.mean(seconds_list)}, Std Dev: {statistics.stdev(seconds_list)}")
    
    else:
        for split in root.findall('Segments/Segment'):
            name = split.find('Name')
            if name is not None and name.text.strip() == prompt2.strip():
                print(name.text)
                split_times = split.findall('SegmentHistory/Time/RealTime')
                
                for split_time in split_times:
                    if split_time is not None:
                        all_split_times.append({
                            "time": split_time.text,
                            "seconds": LSStoSeconds(split_time.text)
                        })

        all_split_times.sort(key=lambda x: x["seconds"])

        seconds_list = [split_time["seconds"] for split_time in all_split_times]
            
        for split in all_split_times:
            print(f"{split['time']}, {100 * (scipy.stats.norm.cdf(split['seconds'], statistics.mean(seconds_list), statistics.stdev(seconds_list))):.3f}%")

        print(f"Mean: {statistics.mean(seconds_list)}, Std Dev: {statistics.stdev(seconds_list)}")

elif prompt1 == "names":
    for split in root.findall('Segments/Segment/Name'):
        print(split.text)


# Variable just to keep the tab open.
tmp = str(input("done"))