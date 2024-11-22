-- init.sql
DO
$$
BEGIN
  IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'astra_db') THEN
    CREATE DATABASE astra_db;
  END IF;
END
$$;

\c astra_db;

CREATE TABLE IF NOT EXISTS department (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS employee (
    id CHAR(8),
    name VARCHAR(100) NOT NULL,
    department_id INT,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    FOREIGN KEY (department_id) REFERENCES department(id) ON DELETE SET NULL
);

INSERT INTO department (name)
VALUES
    ('Sales'),
    ('Human Resources'),
    ('Production Management'),
    ('Product Management');

INSERT INTO employee (id, name, department_id, email, password)
VALUES
    ('A0000001', '田中太郎', 1, 'taro.tanaka@example.com', 'password123'),
    ('A0000002', '鈴木花子', 2, 'hanako.suzuki@example.com', 'password456'),
    ('B0000001', '佐藤次郎', 3, 'jiro.sato@example.com', 'password789'),
    ('C0000001', '高橋美穂', 4, 'miho.takahashi@example.com', 'password1011');