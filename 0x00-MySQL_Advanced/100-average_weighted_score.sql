-- creates a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.
DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
    IN user_id INT
)
BEGIN
    DECLARE total_weighted_score INT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;
    DECLARE avg_weighted_score Float;

    -- Calculate the total weighted score and total weight for the user's projects
    SELECT SUM(c.score * p.weight), SUM(p.weight)
    INTO total_weighted_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- If there are no projects, set the weighted average score to 0 to avoid division by zero
    IF total_weight = 0 THEN
        SET avg_weighted_score = 0;
    ELSE
        -- Compute the weighted average score
        SET avg_weighted_score = total_weighted_score / total_weight;
    END IF;

    -- Update the users table with the computed weighted average score
    UPDATE users
    SET average_score = avg_weighted_score
    WHERE id = user_id;

END $$

DELIMITER ;
