from datetime import timedelta, datetime
from data import tasks


def main():
    print(f"estimated due date: {get_estimated_due_date(tasks)}")
   



def get_estimated_due_date(task_list):
    total_time = 0
    total_difficulty = 0
    for task in task_list:
        if task["completed"] is not None:
            duration_seconds = (task["completed"] - task["started"]).total_seconds()  # duration in seconds
            difficulty = task["difficulty"]
            
            total_time += duration_seconds
            total_difficulty += difficulty    
    
    if total_difficulty == 0:
        return None  
        
    avg_time_per_difficulty = total_time / total_difficulty
    
    seconds_remaining = sum(
        avg_time_per_difficulty * task["difficulty"]
        for task in task_list
        if task["completed"] is None
    )

    estimated_time_remaining = timedelta(seconds=seconds_remaining) 
    return (estimated_time_remaining + datetime.now())


if __name__ == "__main__":
    main()