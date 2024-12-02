# main.py

from user_management.family import FamilyManagement
from user_management.reminder import ReminderSystem
from medication_management.medication import Medication, PrescriptionMedication
from medication_management.inventory import InventoryManagement


if __name__ == "__main__":
    family_manager = FamilyManagement()
    reminder_system = ReminderSystem()

    while True:
        # 自动检查所有家庭成员的低库存药物并提醒
        low_stock_warnings = family_manager.get_all_low_stock()
        if low_stock_warnings:
            print("\n--- Low Stock Alerts ---")
            for member_name, med_id, med_name, days_left in low_stock_warnings:
                message = f"Low stock alert for {member_name}'s {med_name} (ID {med_id})! Only {days_left} days of stock left."
                reminder_system.set_reminder(med_id, message)
            reminder_system.list_reminders()

        print("\n--- MediTrack Menu ---")
        print("1. Add Family Member")
        print("2. Switch to Family Member")
        print("3. List Family Members")
        print("4. Add Medication for Current Member")
        print("5. Update Stock for Current Member")
        print("6. Generate Stock Report for Current Member")
        print("7. List Reminders")
        print("8. Exit")
        print("9. List Prescription Medications")
        print("10. Generate Prescription Report")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter family member's name: ")
            family_manager.add_member(name)

        elif choice == "2":
            name = input("Enter family member's name: ")
            family_manager.switch_member(name)

        elif choice == "3":
            family_manager.list_members()

        elif choice == "4":
            inventory_manager = family_manager.get_current_member_inventory()
            if inventory_manager:
                med_name = input("Enter medication name: ")
                dosage = input("Enter dosage: ")
                frequency = input("Enter frequency: ")
                daily_dosage = int(input("Enter daily dosage: "))
                stock = int(input("Enter stock quantity: "))
                med_type = input("Is this a prescription medication? (yes/no): ").strip().lower()

                if med_type == "yes":
                    doctor_name = input("Enter doctor's name: ")
                    prescription_date = input("Enter prescription date: ")
                    indication = input("Enter indication: ")
                    warnings = input("Enter warnings: ")
                    expiration_date = input("Enter expiration date: ")
                    medication = PrescriptionMedication(
                        med_name, dosage, frequency, daily_dosage, stock,
                        doctor_name, prescription_date, indication, warnings, expiration_date
                    )
                else:
                    medication = Medication(med_name, dosage, frequency, daily_dosage, stock)

                inventory_manager.add_medication(medication)

        elif choice == "5":
            inventory_manager = family_manager.get_current_member_inventory()
            if inventory_manager:
                med_id = int(input("Enter medication ID to update stock: "))
                quantity = int(input("Enter quantity to add (negative to reduce): "))
                inventory_manager.update_stock(med_id, quantity)

        elif choice == "6":
            inventory_manager = family_manager.get_current_member_inventory()
            if inventory_manager:
                inventory_manager.generate_stock_report()

        elif choice == "7":
            reminder_system.list_reminders()

        elif choice == "8":
            print("Exiting MediTrack. Goodbye!")
            break

        elif choice == "9":
            inventory_manager = family_manager.get_current_member_inventory()
            if inventory_manager:
                prescription_meds = inventory_manager.list_prescription_medications()
                for med in prescription_meds:
                    print(med)

        elif choice == "10":
            inventory_manager = family_manager.get_current_member_inventory()
            if inventory_manager:
                inventory_manager.generate_prescription_report()

        else:
            print("Invalid choice. Please try again.")
