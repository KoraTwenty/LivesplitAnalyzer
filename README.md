# Livesplit File Analyzer by KoraTwenty

## General Use

### Before Use:

Place the Python file in the same folder as your `.lss` file is in. This is the sole requirement for this to work. Upon starting the program it should state the directory at the top of the console.

**IMPORTANT! Please ensure you have scipy installed or this will not work! This can be done by running `pip install scipy` inside `cmd.exe`.**

Note: You have to reopen the file every time you want to run it again, I will be solving this in later commits.

### Split File:

Input the name of your livesplit file followed by `.lss`. Ex: `PitOf100Trials.lss`

### Prompt 1:
`c`, `chrono` & `chronological`: Will list off times in chronological order of when they occured.

`r` & `rank`: Will list off times in order of fastest to slowest.

`p`, `prob`, `probability`, `s`, `stat`, `stats` & `statistics`: Will list off times along with the percentile of the run, in order of fastest to slowest.

`names`: Will list all of the split names. (Doesn't give Prompt 2)

## Prompt 2:
`*`, `all` & `run`: Searches over the entire run.

`[Split Name]`: Searches specifically that split.
