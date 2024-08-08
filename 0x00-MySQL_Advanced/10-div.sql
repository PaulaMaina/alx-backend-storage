-- Creates a SafeDiv function
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	DECLARE div_result FLOAT DEFAULT 0;

	IF b != 0 THEN
	    SET div_result = a / b;
	END IF;
	RETURN div_result;
END $$
DELIMITER ;
