-- Computes and scores the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	DECLARE total_score INT DEFAULT 0;
	DECLARE project_count INT DEFAULT 0;

	SELECT SUM(score)
	    INTO total_score
	    FROM corrections
	    WHERE corrections.user_id = user_id;
	SELECT COUNT(*)
	    INTO project_count
	    FROM corrections
	    WHERE corrections.user_id = user_id;
	UPDATE users
	    SET users.average_score = IF(project_count != 0, total_score / project_count, 0)
	    WHERE users.id = user_id;
END $$
DELIMITER ;
