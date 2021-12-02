-- A SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER subtract_item BEFORE INSERT ON orders FOR EACH ROW UPDATE food SET quantity=quantity-NEW.number WHERE name=NEW.item_name;
