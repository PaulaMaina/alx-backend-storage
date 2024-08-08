-- Creates a trigger that resets valid_email only when email is changed
DELIMITER $$
CREATE TRIGGER update_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email != NEW.email THEN
	    SET NEW.valid_email = 0;
	ELSE
	    SET NEW.valid_email = NEW.valid_email;
	END IF;
END $$
DELIMITER ;
