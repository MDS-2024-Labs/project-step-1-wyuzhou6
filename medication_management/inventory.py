# inventory.py

import pandas as pd
from pathlib import Path
from .medication import Medication, PrescriptionMedication

class InventoryManagement:
    def __init__(self, member_name):
        self.member_name = member_name
        self.data_dir = Path("data/inventory")
        self.data_dir.mkdir(exist_ok=True, parents=True)
        
        self.inventory_file = self.data_dir / f"{member_name}_inventory.csv"
        self.history_file = self.data_dir / f"{member_name}_history.csv"
        
        # 初始化数据
        self.medications = {}
        self.next_med_id = 1
        self._load_inventory()

    def _load_inventory(self):
        """从CSV加载库存数据"""
        if not self.inventory_file.exists():
            # 如果文件不存在，创建一个空的DataFrame并保存
            df = pd.DataFrame(columns=[
                'med_id', 'med_name', 'dosage', 'frequency', 'daily_dosage',
                'stock', 'is_prescription', 'doctor_name', 'prescription_date',
                'indication', 'warnings', 'expiration_date'
            ])
            df.to_csv(self.inventory_file, index=False)
            return

        try:
            df = pd.read_csv(self.inventory_file)
            if df.empty:
                return
                
            for _, row in df.iterrows():
                if row['is_prescription']:
                    med = PrescriptionMedication(
                        med_name=row['med_name'],
                        dosage=row['dosage'],
                        frequency=row['frequency'],
                        daily_dosage=row['daily_dosage'],
                        stock=row['stock'],
                        doctor_name=row['doctor_name'],
                        prescription_date=row['prescription_date'],
                        indication=row['indication'],
                        warnings=row['warnings'],
                        expiration_date=row['expiration_date']
                    )
                else:
                    med = Medication(
                        med_name=row['med_name'],
                        dosage=row['dosage'],
                        frequency=row['frequency'],
                        daily_dosage=row['daily_dosage'],
                        stock=row['stock']
                    )
                self.medications[row['med_id']] = med
            
            # 更新next_med_id
            if not df.empty:
                self.next_med_id = df['med_id'].max() + 1
                
        except Exception as e:
            print(f"Error loading inventory for {self.member_name}: {str(e)}")
            # 创建新的空文件
            df = pd.DataFrame(columns=[
                'med_id', 'med_name', 'dosage', 'frequency', 'daily_dosage',
                'stock', 'is_prescription', 'doctor_name', 'prescription_date',
                'indication', 'warnings', 'expiration_date'
            ])
            df.to_csv(self.inventory_file, index=False)

    def _save_inventory(self):
        """保存库存数据到CSV"""
        data = []
        for med_id, med in self.medications.items():
            med_data = med.to_dict()
            med_data['med_id'] = med_id
            med_data['is_prescription'] = isinstance(med, PrescriptionMedication)
            data.append(med_data)
            
        df = pd.DataFrame(data)
        df.to_csv(self.inventory_file, index=False)

    def add_medication(self, medication):
        """添加新药物"""
        med_id = self.next_med_id
        self.medications[med_id] = medication
        self.next_med_id += 1
        
        # 保存更新
        self._save_inventory()
        
        print(f"Medication {medication.med_name} added with ID {med_id}")
        return med_id

    def update_stock(self, med_id, quantity):
        """更新库存"""
        if med_id not in self.medications:
            print(f"Medication ID {med_id} not found")
            return False
            
        medication = self.medications[med_id]
        if medication.update_stock(quantity):
            self._save_inventory()
            return True
        return False

    def check_low_stock(self):
        """检查低库存药物"""
        low_stock = []
        for med_id, medication in self.medications.items():
            days_left = medication.calculate_days_left()
            if days_left is not None and days_left <= 3:
                low_stock.append((med_id, medication.med_name, days_left))
        return low_stock

    def generate_stock_report(self):
        """生成库存报告"""
        if not self.medications:
            print("No medications found.")
            return
            
        print("\nStock Report:")
        print(f"{'ID':<5} {'Name':<20} {'Stock':<10} {'Days Left':<10}")
        print("-" * 50)
        
        for med_id, medication in self.medications.items():
            days_left = medication.calculate_days_left() or "N/A"
            print(f"{med_id:<5} {medication.med_name:<20} {medication.stock:<10} {days_left:<10}")

    def list_prescription_medications(self):
        """列出所有处方药"""
        return [
            {
                "id": med_id,
                "name": med.med_name,
                "doctor": getattr(med, 'doctor_name', 'N/A'),
                "date": getattr(med, 'prescription_date', 'N/A'),
                "indication": getattr(med, 'indication', 'N/A'),
                "warnings": getattr(med, 'warnings', 'N/A'),
                "expiration_date": getattr(med, 'expiration_date', 'N/A')
            }
            for med_id, med in self.medications.items()
            if isinstance(med, PrescriptionMedication)
        ]

    def generate_prescription_report(self):
        """生成处方报告"""
        prescriptions = self.list_prescription_medications()
        if not prescriptions:
            print("No prescription medications found")
            return
            
        print("\nPrescription Report:")
        print(f"{'ID':<5} {'Name':<20} {'Doctor':<15} {'Date':<12} {'Indication':<15} "
              f"{'Warnings':<20} {'Expiration':<12}")
        print("-" * 100)
        
        for med in prescriptions:
            print(f"{med['id']:<5} {med['name']:<20} {med['doctor']:<15} {med['date']:<12} "
                  f"{med['indication']:<15} {med['warnings']:<20} {med['expiration_date']:<12}")
