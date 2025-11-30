# student_management.py
import json
import os
from typing import List, Optional


# ============================
#      სტუდენტის კლასი
# ============================
class Student:
    _roll_counter = 1  # უნიკალური მზარდი ინდექსი, საიდანაც გენერირდება სიის ნომერი

    def __init__(self, name: str, surname: str, score: float, roll_number: Optional[int] = None):
        self.name = name
        self.surname = surname
        self.score = score

        if roll_number is not None:
            self.roll_number = roll_number
        else:
            self.roll_number = Student._roll_counter
            Student._roll_counter += 1

        self.grade = self.calculate_grade(score)

    @staticmethod
    def calculate_grade(score: float) -> str:
        if score >= 91:
            return "A"
        elif score >= 81:
            return "B"
        elif score >= 71:
            return "C"
        elif score >= 61:
            return "D"
        elif score >= 51:
            return "E"
        else:
            return "F"

    def update_score(self, new_score: float):
        self.score = new_score
        self.grade = self.calculate_grade(new_score)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "surname": self.surname,
            "roll_number": self.roll_number,
            "score": self.score,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(d: dict) -> "Student":
        return Student(
            name=d["name"],
            surname=d.get("surname", ""),
            score=float(d["score"]),
            roll_number=int(d["roll_number"])
        )


# ============================
#   სტუდენტების მართვის სისტემა
# ============================
class StudentManager:
    FILE_NAME = "students.json"

    def __init__(self, filename: Optional[str] = None):
        self.FILE_NAME = filename or StudentManager.FILE_NAME
        self.students: List[Student] = []
        self.load_students()

    # --- ვალიდაცია ---
    @staticmethod
    def validate_person_name(value: str) -> bool:
        if not value or not value.strip():
            return False
        v = value.replace(" ", "").replace("-", "")
        return v.isalpha()

    @staticmethod
    def validate_score_value(value: str) -> Optional[float]:
        if value is None:
            return None
        s = value.strip()
        if s == "":
            return None
        try:
            v = float(s)
            if 0 <= v <= 100:
                return v
            return None
        except ValueError:
            return None

    # --- მონაცემების ჩატვირთვა ---
    def load_students(self):
        if not os.path.exists(self.FILE_NAME):
            return

        try:
            if os.path.getsize(self.FILE_NAME) == 0:
                return
        except OSError:
            return

        try:
            with open(self.FILE_NAME, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            print("⚠️ students.json поврежден — создаётся пустой список.")
            return

        max_roll = 0
        for item in data:
            try:
                st = Student.from_dict(item)
            except Exception:
                continue

            self.students.append(st)
            if st.roll_number > max_roll:
                max_roll = st.roll_number

        Student._roll_counter = max_roll + 1

    # --- მონაცემების შენახვა ---
    def save_students(self):
        data = [s.to_dict() for s in self.students]
        try:
            with open(self.FILE_NAME, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except OSError:
            print("❌ შეცდომა მონაცემების შენახვისას.")

    # --- სტუდენტის დამატება ---
    def add_student_data(self, name: str, surname: str, score_value: float) -> Student:
        student = Student(name=name, surname=surname, score=score_value)
        self.students.append(student)
        self.save_students()
        return student

    def add_student(self):
        print("\n--- ახალი სტუდენტის დამატება ---")

        while True:
            name = input("სახელი: ").strip()
            if not StudentManager.validate_person_name(name):
                print("❌ მხოლოდ ასოები ნებადართულია.")
                continue
            break

        while True:
            surname = input("გვარი: ").strip()
            if not StudentManager.validate_person_name(surname):
                print("❌ მხოლოდ ასოები ნებადართულია.")
                continue
            break

        while True:
            score_input = input("ქულა (0-100): ")
            score_value = StudentManager.validate_score_value(score_input)
            if score_value is None:
                print("❌ ქულა უნდა იყოს 0–100.")
                continue
            break

        student = self.add_student_data(name, surname, score_value)
        print(f"\n✅ დაემატა! სიის №: {student.roll_number}\n")

    # --- ყველა სტუდენტი ---
    def view_all_students(self):
        print("\n--- სტუდენტების სია ---")
        if not self.students:
            print("⚠️ სია ცარიელია.")
            return

        for s in self.students:
            print(f"№{s.roll_number} | {s.name} {s.surname} | ქულა: {s.score} | Grade: {s.grade}")

    # --- ძებნა ---
    def search_by_query(self, query: str) -> List[Student]:
        q = (query or "").strip().lower()
        if not q:
            return []

        results = []
        for s in self.students:
            if q in s.name.lower() or q in s.surname.lower() or q in f"{s.name.lower()} {s.surname.lower()}":
                results.append(s)

        return results

    def search_student(self):
        print("\n--- ძებნა ---")
        query = input("ჩაწერეთ სახელი ან გვარი: ").strip()
        results = self.search_by_query(query)

        if not results:
            print("❌ ვერ მოიძებნა.")
            return

        print(f"\n⭐ ნაპოვნია {len(results)} სტუდენტი:\n")
        for s in results:
            print(f"№{s.roll_number} | {s.name} {s.surname} | ქულა: {s.score} | Grade: {s.grade}")

    # --- შეფასების განახლება ---
    def update_grade(self):
        print("\n--- განახლება ---")

        rn_input = input("სიის ნომერი: ").strip()
        if not rn_input.isdigit():
            print("❌ ციფრები შეიყვანეთ!")
            return

        rn = int(rn_input)

        student = next((s for s in self.students if s.roll_number == rn), None)
        if not student:
            print("❌ სტუდენტი ვერ მოიძებნა.")
            return

        while True:
            score_input = input("ახალი ქულა (0–100): ").strip()
            new_score = StudentManager.validate_score_value(score_input)
            if new_score is None:
                print("❌ მიუთითეთ корректული ქულა.")
                continue
            break

        student.update_score(new_score)
        self.save_students()
        print("✅ განახლებულია!")

    # --- მენიუ ---
    def menu(self):
        while True:
            print("\n======= Students Management System =======")
            print("1. სტუდენტის დამატება")
            print("2. სტუდენტების ნახვა")
            print("3. ძებნა")
            print("4. შეფასების განახლება")
            print("5. გასვლა")
            print("==========================================")

            choice = input("აირჩიეთ ოპერაცია: ").strip()

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_all_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_grade()
            elif choice == "5":
                print("👋 ნახვამდის!")
                break
            else:
                print("❌ არასწორი არჩევანი.")


# ============================
#       პროგრამის გაშვება
# ============================
if __name__ == "__main__":
    manager = StudentManager()
    manager.menu()
