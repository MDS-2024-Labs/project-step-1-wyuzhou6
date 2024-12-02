# medication.py

class Medication:
    def __init__(self, med_name, dosage, frequency, daily_dosage, stock):
        self.med_name = med_name
        self.dosage = dosage
        self.frequency = frequency
        self.daily_dosage = daily_dosage
        self.stock = stock

    def get_medication_info(self):
        return {
            "name": self.med_name,
            "dosage": self.dosage,
            "frequency": self.frequency,
            "daily_dosage": self.daily_dosage,
            "stock": self.stock,
        }

    def update_stock(self, quantity):
        new_stock = self.stock + quantity
        if new_stock < 0:
            print(f"Cannot update stock: insufficient stock.")
            return False
        self.stock = new_stock
        return True

    def calculate_days_left(self):
        if self.daily_dosage == 0:
            print("Daily dosage is not set.")
            return None
        return self.stock // self.daily_dosage


class PrescriptionMedication(Medication):
    def __init__(self, med_name, dosage, frequency, daily_dosage, stock, doctor_name, prescription_date, indication=None, warnings=None, expiration_date=None, feedback=None):
        super().__init__(med_name, dosage, frequency, daily_dosage, stock)
        self.doctor_name = doctor_name
        self.prescription_date = prescription_date
        self.indication = indication
        self.warnings = warnings
        self.expiration_date = expiration_date
        self.feedback = feedback

    def is_prescription_valid(self):
        from datetime import datetime
        if self.expiration_date:
            expiration = datetime.strptime(self.expiration_date, "%Y-%m-%d")
            return expiration > datetime.now()
        return True

    def add_feedback(self, feedback):
        self.feedback = feedback

    def get_prescription_info(self):
        return {
            "doctor_name": self.doctor_name,
            "prescription_date": self.prescription_date,
            "indication": self.indication,
            "warnings": self.warnings,
            "expiration_date": self.expiration_date,
            "feedback": self.feedback or "No feedback yet.",
        }
