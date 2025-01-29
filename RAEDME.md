## Setup for Django × PostfreSQL on DevContainer


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
INSERT INTO orders(id, customer_id, item_id, quantity, order_date)
VALUES
(1, 'C0000001', 'C1I00001', 50, '2025-01-15'),
(2, 'C0000002', 'C1I00002', 60, '2025-01-16'),
(3, 'C0000003', 'C1I00003', 70, '2025-01-17'),
(4, 'C0000004', 'C2I00001', 80, '2025-01-18'),
(5, 'C0000005', 'C2I00002', 90, '2025-01-19'),
(6, 'C0000006', 'C3I00001', 100, '2025-01-20'),
(7, 'C0000007', 'C3I00002', 110, '2025-01-21'),
(8, 'C0000008', 'C3I00003', 120, '2025-01-22'),
(9, 'C0000009', 'C4I00001', 130, '2025-01-23'),
(10, 'C0000010', 'C4I00002', 140, '2025-01-24');
```

3. Insert production data:
```sql
INSERT INTO production (id, order_id, lot_quantity, due_date, estimated_completion_date, completion_date) 
VALUES
(1, 6, 100, '2025-02-20', '2025-03-01', '2025-03-02'),
(2, 10, 150, '2025-02-21', '2025-03-03', NULL),
(3, 3, 120, '2025-02-22', '2025-03-05', '2025-03-06'),
(4, 9, 130, '2025-02-23', '2025-03-07', '2025-03-08'),
(5, 5, 110, '2025-02-24', '2025-03-09', NULL),
(6, 8, 140, '2025-02-25', '2025-03-11', '2025-03-12'),
(7, 7, 160, '2025-02-26', '2025-03-13', '2025-03-14'),
(8, 1, 170, '2025-02-27', '2025-03-15', '2025-03-16'),
(9, 4, 180, '2025-02-28', '2025-03-17', '2025-03-18'),
(10, 2, 190, '2025-03-01', '2025-03-19', NULL);
```