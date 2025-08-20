import os
import re

from qr_generator import QR_generator

class Student:
    def __init__(self, name: str, address: str, age: str, grade: str):
        self.name = name
        self.address = address
        self.age = age
        self.grade = grade

    @staticmethod
    def add_student():
        name = input("Enter Student Name: ").strip()
        address = input("Enter Address: ").strip()
        age = input("Enter Age: ").strip()
        grade = input("Enter Grade: ").strip()

        s = Student(name, address, age, grade)

        filepath = s.save_to_file()
        qr_text = s.to_qr_string(filepath)
        qr_file = s.qr_path()
        
        qr_gen = QR_generator(qr_text, qr_file)
        qr_gen.generate_qr()

        print(f"✅ Student data saved in {filepath}")
        print(f"✅ QR code saved in {qr_file}")

    def _slug(self) -> str:
        base = f"{self.name}".strip()
        slug = re.sub(r'[^A-Za-z0-9._-]+', '_', base)
        return slug or "student"

    def file_path(self) -> str:
        os.makedirs("students", exist_ok=True)
        return os.path.join("students", f"{self._slug()}.txt")

    def qr_path(self) -> str:
        os.makedirs("students", exist_ok=True)
        return os.path.join("students", f"{self._slug()}_qr.png")

    def save_to_file(self) -> str:
        path = self.file_path()
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"Name: {self.name}\n")
            f.write(f"Address: {self.address}\n")
            f.write(f"Age: {self.age}\n")
            f.write(f"Grade: {self.grade}\n")
        return path

    def to_qr_string(self, filepath: str) -> str:
        return (
            f"Name: {self.name}\n"
            f"Address: {self.address}\n"
            f"Age: {self.age}\n"
            f"Grade: {self.grade}\n"
            f"File: {filepath}"
        )
