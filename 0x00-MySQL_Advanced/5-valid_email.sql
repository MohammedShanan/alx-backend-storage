-- Validates a user's email upon update by resetting
-- the `valid_email` field if the email changes.
DROP TRIGGER IF EXISTS validate_email;
DELIMITER $$
CREATE TRIGGER validate_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email is being updated
    IF OLD.email != NEW.email THEN
        -- Mark the new email as not validated
        SET NEW.valid_email = 0;
    END IF;
END $$
DELIMITER ;
