# inventory.py

from .medication import Medication, PrescriptionMedication

class InventoryManagement:
    def __init__(self):
        self.medications = {}
        self.next_med_id = 1

    def add_medication(self, medication):
        med_id = self.next_med_id
        self.medications[med_id] = medication
        self.next_med_id += 1
        print(f"Medication {medication.med_name} added with ID {med_id}.")
        return med_id

    def update_stock(self, med_id, quantity):
        if med_id in self.medications:
            medication = self.medications[med_id]
            return medication.update_stock(quantity)
        print(f"Medication ID {med_id} not found.")
        return False

    def check_low_stock(self):
        low_stock = []
        for med_id, medication in self.medications.items():
            days_left = medication.calculate_days_left()
            if days_left is not None and days_left <= 3:
                low_stock.append((med_id, medication.med_name, days_left))
        return low_stock

    def generate_stock_report(self):
        print("Stock Report:")
        print(f"{'ID':<5} {'Name':<20} {'Stock':<10} {'Days Left':<10}")
        print("-" * 50)
        for med_id, medication in self.medications.items():
            days_left = medication.calculate_days_left() or "N/A"
            print(f"{med_id:<5} {medication.med_name:<20} {medication.stock:<10} {days_left:<10}")

    def list_prescription_medications(self):
        return [
            {
                "id": med_id,
                "name": medication.med_name,
                "doctor": medication.doctor_name,
                "date": medication.prescription_date,
                "indication": getattr(medication, "indication", "N/A"),
                "warnings": getattr(medication, "warnings", "N/A"),
                "expiration_date": getattr(medication, "expiration_date", "N/A"),
                "feedback": getattr(medication, "feedback", "No feedback yet."),
            }
            for med_id, medication in self.medications.items()
            if isinstance(medication, PrescriptionMedication)
        ]

    def generate_prescription_report(self):
        report = self.list_prescription_medications()
        if not report:
            print("No prescription medications found.")
            return
        print("Prescription Report:")
        print(f"{'ID':<5} {'Name':<20} {'Doctor':<15} {'Date':<12} {'Indication':<15} {'Warnings':<20} {'Expiration':<12} {'Feedback':<15}")
        print("-" * 120)
        for item in report:
            print(f"{item['id']:<5} {item['name']:<20} {item['doctor']:<15} {item['date']:<12} {item['indication']:<15} "
                  f"{item['warnings']:<20} {item['expiration_date']:<12} {item['feedback'] or 'N/A':<15}")
