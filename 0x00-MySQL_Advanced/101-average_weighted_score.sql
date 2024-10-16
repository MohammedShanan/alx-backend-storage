-- Creates a stored procedure ComputeAverageWeightedScoreForUsers that
-- computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    SET average_score = IFNULL((
        SELECT SUM(c.score * p.weight) / SUM(p.weight)
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = users.id
    ), 0);
    
END $$

DELIMITER ;