-- Computes and scores the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
	DECLARE total_weighted_score INT DEFAULT 0;
	DECLARE weight_total INT DEFAULT 0;

	SELECT SUM(corrections.score * projects.weight)
	    INTO total_weighted_score
	    FROM corrections
	        INNER JOIN projects
		    ON corrections.project_id = projects.id
	    WHERE corrections.user_id = user_id;
	SELECT SUM(projects.weight)
	    INTO weight_total
	    FROM corrections
	        INNER JOIN projects
		    ON corrections.project_id = projects.id
	    WHERE corrections.user_id = user_id;

	IF weight_total != 0 THEN
	    UPDATE users
	        SET users.average_score = total_weighted_score / weight_total
	        WHERE users.id = user_id;
	ELSE
	    UPDATE users
	        SET users.average_score = 0
	        WHERE users.id = user_id;
	END IF;
END $$
DELIMITER ;
