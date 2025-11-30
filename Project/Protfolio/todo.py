from datetime import datetime

class DailyRoutineManager:
    def __init__(self):
        self.water_target = 3.5
        self.calorie_limit = 1600
        self.protein_target = 110
        
        self.water_consumed = 0.0
        self.calories_consumed = 0
        self.protein_consumed = 0
        self.completed_tasks = []
        
        self.time_blocks = {
            "Morning": {
                "time": "7:00 AM - 12:00 PM",
                "water": 1.0,
                "calories": 400,
                "protein": 30,
                "tasks": ["Morning hygiene", "Plan the day", "Breakfast"]
            },
            "Gym": {
                "time": "12:00 PM - 2:00 PM",
                "water": 0.5,
                "calories": 0,
                "protein": 0,
                "tasks": ["Workout", "Cool down", "Rest"]
            },
            "Coding Class": {
                "time": "2:30 PM - 3:30 PM",
                "water": 0.3,
                "calories": 100,
                "protein": 0,
                "tasks": ["Attend class", "Take notes", "Ask doubts"]
            },
            "Practice": {
                "time": "3:30 PM - 4:30 PM",
                "water": 0.2,
                "calories": 0,
                "protein": 0,
                "tasks": ["Code practice", "Review notes"]
            },
            "Duty": {
                "time": "5:00 PM - 10:30 PM",
                "water": 1.0,
                "calories": 500,
                "protein": 30,
                "tasks": ["FO duty tasks", "Stay alert", "Snack time"]
            },
            "Night": {
                "time": "10:00 PM - 11:00 PM",
                "water": 0.5,
                "calories": 600,
                "protein": 50,
                "tasks": ["Dinner", "Meditation", "Sleep prep"]
            }
        }
    
    def get_current_block(self):
        """Fixed time block detection"""
        current_hour = datetime.now().hour
        current_minute = datetime.now().minute
        
        if 7 <= current_hour < 12:
            return "Morning"
        elif 12 <= current_hour < 14:
            return "Gym"
        elif current_hour == 14 and current_minute >= 30:
            return "Coding Class"
        elif current_hour == 15 and current_minute < 30:
            return "Coding Class"
        elif (current_hour == 15 and current_minute >= 30) or (current_hour == 16 and current_minute < 30):
            return "Practice"
        elif 17 <= current_hour < 22:
            return "Duty"
        else:
            return "Night"
    
    def show_current_block(self):
        """Display current block info"""
        block = self.get_current_block()
        info = self.time_blocks[block]
        
        print("\n" + "="*50)
        print("Current Block: " + block)
        print("Time: " + info["time"])
        print("="*50)
        print("\nSuggested for this block:")
        print("Water: " + str(info["water"]) + "L")
        print("Calories: " + str(info["calories"]) + " kcal")
        print("Protein: " + str(info["protein"]) + "g")
        print("\nTasks:")
        for i, task in enumerate(info["tasks"], 1):
            status = "✓" if task in self.completed_tasks else "○"
            print(str(i) + ". " + status + " " + task)
    
    def add_water(self):
        """Track water with validation"""
        try:
            amount = float(input("\nWater intake (in ml): "))
            
            if amount < 0:
                print("\n✗ Invalid! Water cannot be negative!")
                return
            
            if amount > 2000:
                confirm = input("That's a lot! Sure? (y/n): ")
                if confirm.lower() != 'y':
                    return
            
            liters = amount / 1000
            self.water_consumed += liters
            
            remaining = self.water_target - self.water_consumed
            
            print("\n✓ Water added: " + str(amount) + " ml")
            print("Total today: " + str(round(self.water_consumed, 2)) + "L / " + str(self.water_target) + "L")
            
            if remaining > 0:
                print("Remaining: " + str(round(remaining, 2)) + "L")
            elif abs(remaining) < 0.1:
                print("Perfect! Target achieved!")
            else:
                print("Warning: Over hydration by " + str(abs(round(remaining, 2))) + "L")
        
        except ValueError:
            print("\n✗ Please enter valid number")
    
    def add_meal(self):
        """Track meal with block-based comparison"""
        print("\n--- Add Meal ---")
        
        current_block = self.get_current_block()
        block_info = self.time_blocks[current_block]
        
        meal_name = input("Meal name: ")
        
        try:
            calories = int(input("Calories: "))
            protein = int(input("Protein (g): "))
            
            if calories < 0 or protein < 0:
                print("\n✗ Invalid! Values cannot be negative!")
                return
            
            self.calories_consumed += calories
            self.protein_consumed += protein
            
            print("\n✓ " + meal_name + " added!")
            print("\nDaily Progress:")
            print("Calories: " + str(self.calories_consumed) + " / " + str(self.calorie_limit) + " kcal")
            print("Protein: " + str(self.protein_consumed) + " / " + str(self.protein_target) + "g")
            
            print("\nBlock Suggestion (" + current_block + "):")
            print("Block target - Calories: " + str(block_info["calories"]) + " kcal")
            print("Block target - Protein: " + str(block_info["protein"]) + "g")
            
            cal_remaining = self.calorie_limit - self.calories_consumed
            pro_remaining = self.protein_target - self.protein_consumed
            
            if cal_remaining > 0:
                print("\nYou can eat " + str(cal_remaining) + " more calories today")
            elif cal_remaining == 0:
                print("\nPerfect calorie balance!")
            else:
                print("\nWarning: Over limit by " + str(abs(cal_remaining)) + " kcal!")
            
            if pro_remaining > 0:
                print("Need " + str(pro_remaining) + "g more protein")
            else:
                print("Protein target achieved!")
        
        except ValueError:
            print("\n✗ Please enter valid numbers")
    
    def complete_task(self):
        """Mark task complete"""
        block = self.get_current_block()
        tasks = self.time_blocks[block]["tasks"]
        
        print("\n--- Tasks for " + block + " ---")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task in self.completed_tasks else "○"
            print(str(i) + ". " + status + " " + task)
        
        try:
            choice = int(input("\nSelect task number to complete: "))
            if 1 <= choice <= len(tasks):
                task = tasks[choice - 1]
                if task not in self.completed_tasks:
                    self.completed_tasks.append(task)
                    print("\n✓ Task completed: " + task)
                    
                    remaining = [t for t in tasks if t not in self.completed_tasks]
                    if remaining:
                        print("Next task: " + remaining[0])
                    else:
                        print("All tasks for this block completed!")
                else:
                    print("\n✗ Task already completed!")
            else:
                print("\n✗ Invalid task number")
        except ValueError:
            print("\n✗ Please enter valid number")
    
    def reset_day(self):
        """Reset all daily data"""
        confirm = input("\nReset all data for new day? (y/n): ")
        if confirm.lower() == 'y':
            self.water_consumed = 0.0
            self.calories_consumed = 0
            self.protein_consumed = 0
            self.completed_tasks.clear()
            print("\n✓ Day reset! Fresh start!")
        else:
            print("\n✗ Reset cancelled")
    
    def show_summary(self):
        """Clean daily summary"""
        print("\n" + "="*50)
        print("           DAILY SUMMARY")
        print("="*50)
        
        water_percent = (self.water_consumed / self.water_target) * 100
        print("\nWater: " + str(round(self.water_consumed, 2)) + "L / " + str(self.water_target) + "L")
        print("Progress: " + str(round(water_percent, 1)) + "%")
        
        cal_percent = (self.calories_consumed / self.calorie_limit) * 100
        print("\nCalories: " + str(self.calories_consumed) + " / " + str(self.calorie_limit) + " kcal")
        print("Progress: " + str(round(cal_percent, 1)) + "%")
        
        pro_percent = (self.protein_consumed / self.protein_target) * 100
        print("\nProtein: " + str(self.protein_consumed) + "g / " + str(self.protein_target) + "g")
        print("Progress: " + str(round(pro_percent, 1)) + "%")
        
        total_tasks = sum(len(block["tasks"]) for block in self.time_blocks.values())
        completed = len(self.completed_tasks)
        task_percent = (completed / total_tasks) * 100 if total_tasks > 0 else 0
        print("\nTasks: " + str(completed) + " / " + str(total_tasks))
        print("Progress: " + str(round(task_percent, 1)) + "%")
        
        avg_score = (water_percent + cal_percent + pro_percent + task_percent) / 4
        print("\n" + "="*50)
        print("DISCIPLINE SCORE: " + str(round(avg_score, 1)) + "%")
        print("="*50)
        
        if avg_score >= 90:
            print("\n🔥 Excellent! Keep it up!")
        elif avg_score >= 75:
            print("\n💪 Good progress! Almost there!")
        elif avg_score >= 60:
            print("\n👍 Not bad. Push harder tomorrow!")
        else:
            print("\n⚡ Need improvement. Don't give up!")
    
    def show_menu(self):
        """Main menu"""
        print("\n" + "="*50)
        print("       DAILY ROUTINE MANAGER")
        print("       by Amit Mondal")
        print("="*50)
        print("\n1. Show Current Block")
        print("2. Add Water Intake")
        print("3. Add Meal")
        print("4. Complete Task")
        print("5. View Daily Summary")
        print("6. Reset Day")
        print("7. Exit")
        print("="*50)
    
    def run(self):
        """Main program"""
        print("\n" + "="*50)
        print("   Welcome to Daily Routine Manager!")
        print("="*50)
        print("\nYour Daily Targets:")
        print("Water: " + str(self.water_target) + "L")
        print("Calories: " + str(self.calorie_limit) + " kcal")
        print("Protein: " + str(self.protein_target) + "g")
        
        while True:
            self.show_menu()
            choice = input("\nEnter choice (1-7): ")
            
            if choice == '1':
                self.show_current_block()
            elif choice == '2':
                self.add_water()
            elif choice == '3':
                self.add_meal()
            elif choice == '4':
                self.complete_task()
            elif choice == '5':
                self.show_summary()
            elif choice == '6':
                self.reset_day()
            elif choice == '7':
                print("\n" + "="*50)
                print("  Thanks for using Routine Manager!")
                print("  Stay disciplined!")
                print("="*50)
                break
            else:
                print("\n✗ Invalid choice! Please select 1-7.")
            
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    manager = DailyRoutineManager()
    manager.run()
