import os
import fastf1

year = 2026
# This pulls the actual 2026 calendar from the F1 API
schedule = fastf1.get_event_schedule(year)

# Filter out testing/pre-season events
races = schedule[schedule['EventFormat'] != 'testing']

for i, row in enumerate(races.itertuples(), 1):
    # Create name like "R01_Australian_Grand_Prix"
    race_name = row.EventName.replace(' ', '_')
    race_folder = f"R{i:02d}_{race_name}"
    
    # Check if it's a Sprint weekend to adjust subfolders
    if row.EventFormat == 'sprint':
        sessions = ['Practice_1', 'Qualifying', 'Sprint_Shootout', 'Sprint', 'Race']
    else:
        sessions = ['Practice_1', 'Practice_2', 'Practice_3', 'Qualifying', 'Race']

    for session in sessions:
        path = os.path.join("2026_Season", race_folder, session)
        os.makedirs(path, exist_ok=True)
        # Create .gitkeep so GitHub tracks the empty folders
        with open(os.path.join(path, ".gitkeep"), "w") as f:
            pass

print("2026 Season structure created successfully.")