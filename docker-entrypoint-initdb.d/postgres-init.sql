create database "curotec";

\c "curotec";

CREATE TABLE commodity_orders (
    order_id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id INT NOT NULL,
    commodity_name VARCHAR(100) NOT NULL,
    order_amount NUMERIC(12, 2) NOT NULL,
    quantity INT NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO commodity_orders (user_id, commodity_name, order_amount, quantity, unit_price, created_at, updated_at, order_id) VALUES (1, 'gold', 5000.00, 10, 500.00, NOW(), NOW(), '123e4567-e89b-12d3-a456-426614174000');
INSERT INTO commodity_orders (user_id, commodity_name, order_amount, quantity, unit_price, created_at, updated_at, order_id) VALUES (1, 'lumber', 995.00, 3, 2985.00, NOW(), NOW(), '123e4567-e89b-12d3-a456-426614174000'),
INSERT INTO commodity_orders (user_id, commodity_name, order_amount, quantity, unit_price, created_at, updated_at, order_id) VALUES (2, 'platinum', 7000.00, 14, 500.00, NOW(), NOW(), '223e4567-e89b-12d3-a456-426614174001');
INSERT INTO commodity_orders (user_id, commodity_name, order_amount, quantity, unit_price, created_at, updated_at, order_id) VALUES (3, 'lean_hogs', 3000.00, 15, 200.00, NOW(), NOW(), '323e4567-e89b-12d3-a456-426614174002');