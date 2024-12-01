This is the DATA533 project developed by Yuzhou Wang and Yubo Wang.


# Family Medication Management System (FamilyMedT)

## Overview

**FamilyMedT** is a system designed to help families manage medications, track inventory, set reminders, and generate detailed reports. It is particularly useful for multi-member households, ensuring medication schedules are followed, inventory is maintained, and misuse or emergencies are avoided.

---

## Key Features by Modules

### 1. Medication Management Module
This module focuses on handling all details related to medications and prescriptions.

- **Core Functions**:
  - **Initialize Medication and Prescription**: Input and save details such as medication name, dosage, frequency, quantity, expiration date, and associated doctor information.
  - **Retrieve Medication Information**: View details of stored medications, including name, dosage, and prescription notes.
  - **Delete Medication Information**: Remove outdated or incorrect medication records.

---

### 2. Inventory Management Module
This module ensures that the medication stock is maintained and alerts are provided when inventory is low.

- **Core Functions**:
  - **Add Medication Information**: Input medication name and initial stock quantity.
  - **Update Medication Stock**: Adjust stock levels based on usage or purchases.
  - **Generate Medication Report**: Create a summary of current inventory and highlight medications that need replenishment.

---

### 3. Family Member Management Module
This module handles user profiles for individual family members and links them to medication logs.

- **Core Functions**:
  - **Add Family Member**: Register a new family member with their personal details.
  - **Switch User Profiles**: Toggle between family member profiles to view their medication schedules and logs.
  - **List All Members**: Display a list of all registered family members and their associated medication logs.

---

### 4. Reminder Module
This module focuses on alerts and reminders to avoid medication misuse and ensure timely refills.

- **Core Functions**:
  - **Automatic Detection for Low Stock and Expirations**: Automatically track medications with less than 4 days of supply or nearing expiration.
  - **Set Custom Reminders**: Create reminders for specific medications based on special requirements.
  - **List All Active Reminders**: Display all current reminders for low-stock or expiring medications across all family members.

---

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MDS-2024-Labs/project-step-1-wyuzhou6.git
   cd FamilyMedT
   ```

2. **Run the Program**:
   Make sure you have Python 3.8 or higher installed, then execute:
   ```bash
   python main.py
   ```

3. **Example Commands**:
   - Add medication:
     ```bash
     python main.py --add-medication "Paracetamol" --quantity 10 --expiration "2024-12-31"
     ```
   - Generate inventory report:
     ```bash
     python main.py --generate-report
     ```

---

## File Structure

```plaintext
FamilyMedT/
├── main.py              # Main application file
├── modules/             # Core functional modules
│   ├── medication.py    # Handles medication-related logic
│   ├── inventory.py     # Manages inventory stock and reporting
│   ├── reminder.py      # Generates alerts and reminders
│   └── family.py          # Manages family member profiles
└── README.md            # Documentation

```

---