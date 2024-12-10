This is the project:FamilyMedT - Family Medication Tracking System,Developed by Yuzhou Wang and Yubo Wang.

# FamilyMedT System README

## System Overview
FamilyMedT is a family medication tracking system that helps manage medications for multiple family members. The system provides functionality for medication inventory management, prescription tracking, and low stock alerts.

## Core Components

### 1. User Management
#### FamilyManagement Class
- **Purpose**: Manages family members and their associated medication inventories
- **Key Functions**:
  - `add_member(name)`: Adds a new family member
  - `switch_member(name)`: Switches active user and checks their medication status
  - `delete_member(name)`: Removes a member and their associated data
  - `get_current_member_inventory()`: Retrieves current member's medication inventory

### 2. Medication Management
#### Medication Class
- **Purpose**: Base class for all medications
- **Properties**:
  - name: Medication name
  - dosage: Medication dosage (e.g., "50mg")
  - frequency: How often to take (e.g., "twice daily")
  - daily_dosage: Number of pills per day
  - stock: Current quantity available
- **Key Functions**:
  - `calculate_days_left()`: Calculates remaining days of medication
  - `update_stock(quantity)`: Updates current stock level

#### PrescriptionMedication Class (extends Medication)
- **Additional Properties**:
  - doctor_name: Prescribing doctor
  - prescription_date: Date prescribed
  - expiration_date: Medication expiry date
  - indication: Usage indication
  - warnings: Important warnings
- **Additional Functions**:
  - `is_expired()`: Checks if medication has expired
  - `display_prescription_info()`: Shows detailed prescription information

### 3. Inventory Management
#### InventoryManagement Class
- **Purpose**: Manages medication inventory for each family member
- **Key Functions**:
  - `add_medication(medication)`: Adds new medication to inventory
  - `update_stock(med_id, quantity)`: Updates medication stock
  - `check_low_stock()`: Identifies medications with ≤3 days supply
  - `generate_stock_report()`: Creates inventory status report
  - `generate_prescription_report()`: Creates prescription medications report
  - `delete_medication(med_id)`: Removes medication from inventory

### 4. Reminder System
#### ReminderSystem Class
- **Purpose**: Manages medication alerts and notifications
- **Key Functions**:
  - `set_reminder(member, med_id, message)`: Creates new reminder
  - `check_alerts(member, low_stock_warnings)`: Processes low stock alerts
  - `clear_reminder(member, med_id)`: Removes specific reminder
  - `list_reminders(member)`: Shows member's active reminders
  - `list_all_reminders()`: Displays all system reminders

## Data Storage
- All data is stored in CSV files in a 'data' directory
- Separate files for:
  - Members list
  - Individual member inventories
  - Reminder records

## Key Features
1. **Multi-user Support**: Manages medications for multiple family members
2. **Prescription Tracking**: Special handling for prescription medications
3. **Automatic Alerts**: Proactive notifications for low stock (≤3 days supply)
4. **Stock Management**: Tracks medication quantities and usage
5. **Report Generation**: Creates inventory and prescription reports
6. **Data Persistence**: Saves all data between sessions

## System Workflow
1. System initialization loads existing data
2. User selects family member
3. System automatically checks medication stock
4. Low stock triggers automatic reminders
5. Users can manage medications and view reports
6. All changes are automatically saved

## Error Handling
- Input validation for all user inputs
- Exception handling for file operations
- Graceful handling of invalid data
- Data consistency checks during operations


