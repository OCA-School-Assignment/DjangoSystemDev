## Setup for Django × PostgreSQL on DevContainer


### Prerequisites
- Ensure you have **Docker** and **VSCode with Dev Containers extension** installed.


### Step 1: Open in DevContainer
1. Open VSCode
2. Press `Cmd + Shift + P`
3. Type `Reopen in Container` and press Enter.


### Step 2: Install Extensions
1. Open **Extensions** (left sidebar).
2. Search and install:
    - **Python** 
    - **Python Debugger**

※ You might need to reload the window


### Step 3: Database Setup
1. Navigate to the app directory:
```bash
cd app
```

2. Run the following commands:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Load initial data:
```bash
python manage.py loaddata ./initial.data.json
```
- Just ignore `initial.data.order.json` & `initial.data.production.json`.
- Instead, insert data manually using the SQL statements below.


### Step 4: Insert Data Manually
1. Open the PostgreSQL shell:
```bash
python manage.py dbshell
```
or
```bash
docker exec -it djangosystemdevassignment-db-1 psql -h db -U astra -d astra_db -p 5432
Password for astra user: astra@123
```

2. Insert orders data:
```sql
INSERT INTO orders(customer_id, item_id, quantity, order_date, estimated_delivery_date, delivery_date)
VALUES
('C0000001', 'C1I00001', 50, '2025-02-15', '2025-03-23', '2025-03-22'),
('C0000001', 'C1I00002', 60, '2025-07-15', '2025-08-20', '2025-08-19'),
('C0000001', 'C1I00003', 70, '2026-01-10', '2026-03-15', '2026-03-14'),
('C0000001', 'C2I00001', 80, '2027-04-01', '2027-06-15', '2027-06-14'),
('C0000002', 'C1I00001', 90, '2025-02-16', '2025-03-01', '2025-02-28'),
('C0000002', 'C1I00002', 100, '2026-06-01', '2026-08-10', '2026-08-09'),
('C0000002', 'C2I00001', 110, '2027-01-22', '2027-03-05', '2027-03-04'),
('C0000002', 'C2I00002', 120, '2027-08-15', '2027-10-01', '2027-09-30'),
('C0000003', 'C3I00001', 130, '2025-03-20', '2025-05-10', '2025-05-09'),
('C0000003', 'C3I00002', 140, '2026-02-18', '2026-04-01', '2026-03-31'),
('C0000003', 'C3I00003', 150, '2027-09-25', '2027-11-10', '2027-11-09'),
('C0000003', 'C4I00001', 160, '2025-05-10', '2025-06-15', '2025-06-14'),
('C0000004', 'C4I00002', 170, '2026-03-01', '2026-04-10', '2026-04-09'),
('C0000004', 'C1I00001', 180, '2027-02-14', '2027-04-01', '2027-03-31'),
('C0000004', 'C1I00002', 190, '2025-06-12', '2025-07-25', '2025-07-24'),
('C0000005', 'C2I00001', 200, '2025-04-25', '2025-06-05', '2025-06-04'),
('C0000005', 'C2I00002', 210, '2026-04-28', '2026-06-15', '2026-06-14'),
('C0000005', 'C3I00001', 220, '2027-05-01', '2027-07-10', '2027-07-09'),
('C0000005', 'C3I00002', 230, '2025-08-07', '2025-09-15', '2025-09-14'),
('C0000006', 'C3I00003', 240, '2026-05-20', '2026-07-01', '2026-06-30'),
('C0000006', 'C4I00001', 250, '2027-06-10', '2027-07-20', '2027-07-19'),
('C0000006', 'C4I00002', 260, '2025-09-01', '2025-10-10', '2025-10-09'),
('C0000006', 'C1I00001', 270, '2026-08-02', '2026-09-12', '2026-09-11'),
('C0000007', 'C1I00002', 280, '2027-07-15', '2027-09-05', '2027-09-04'),
('C0000007', 'C1I00003', 290, '2025-10-25', '2025-12-01', '2025-11-30'),
('C0000007', 'C2I00001', 300, '2026-09-10', '2026-10-15', '2026-10-14'),
('C0000007', 'C2I00002', 310, '2027-10-01', '2027-11-15', '2027-11-14'),
('C0000008', 'C3I00001', 320, '2025-11-05', '2025-12-15', '2025-12-14'),
('C0000008', 'C3I00002', 330, '2026-10-12', '2026-11-20', '2026-11-19'),
('C0000008', 'C3I00003', 340, '2027-11-10', '2027-12-15', '2027-12-14'),
('C0000008', 'C4I00001', 350, '2025-12-18', '2026-02-01', '2026-01-31'),
('C0000009', 'C4I00002', 360, '2026-11-01', '2026-12-10', '2026-12-09'),
('C0000009', 'C1I00001', 370, '2027-12-20', '2028-02-10', '2028-02-09'),
('C0000009', 'C1I00002', 380, '2025-12-30', '2026-02-01', '2026-01-31'),
('C0000009', 'C2I00001', 390, '2026-12-25', '2027-02-15', '2027-02-14'),
('C0000010', 'C2I00002', 400, '2025-01-05', '2025-02-20', '2025-02-19'),
('C0000010', 'C3I00001', 410, '2026-01-25', '2026-03-05', '2026-03-04'),
('C0000010', 'C3I00002', 420, '2027-02-20', '2027-04-01', '2027-03-31'),
('C0000010', 'C4I00001', 430, '2025-03-10', '2025-04-15', '2025-04-14');
```

3. Insert production data:
```sql
INSERT INTO production (order_id, lot_quantity, due_date, estimated_completion_date, completion_date) 
VALUES
(6, 100, '2025-02-20', '2025-03-01', '2025-03-02'),
(10, 150, '2025-02-21', '2025-03-03', NULL),
(3, 120, '2025-02-22', '2025-03-05', '2025-03-06'),
(9, 130, '2025-02-23', '2025-03-07', '2025-03-08'),
(5, 110, '2025-02-24', '2025-03-09', NULL),
(8, 140, '2025-02-25', '2025-03-11', '2025-03-12'),
(7, 160, '2025-02-26', '2025-03-13', '2025-03-14'),
(1, 170, '2025-02-27', '2025-03-15', '2025-03-16'),
(4, 180, '2025-02-28', '2025-03-17', '2025-03-18'),
(2, 190, '2025-03-01', '2025-03-19', NULL);
```


### Step 5: Start Tailwind
```bash
python manage.py tailwind start
```
