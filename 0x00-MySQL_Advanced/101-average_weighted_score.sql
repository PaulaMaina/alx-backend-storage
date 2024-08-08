-- Computes and sstores the average weighted score for all students
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
	ALTER TABLE users ADD total_weighted_score INT NOT NULL;
	ALTER TABLE users ADD weight_total INT NOT NULL;

	UPDATE users
	    SET total_weighted_score = (
		SELECT SUM(corrections.score * projects.weight)
		FROM corrections
		    INNER JOIN projects
		        ON corrections.project_id = projects.id
		WHERE correction.user_id = users.id
	    );
	UPDATE users
	    SET weight_total = (
		SELECT SUM(projects.weight)
		FROM corrections
		    INNER JOIN projects
		        ON corrections.project_id = projects.id
		WHERE corrections.user_id = users.id
	    );
	UPDATE users
	    SET users.average_score = IF(users.weight_total != 0, users.total_weighted_score / users.weight_total, 0);
	ALTER TABLE users
	    DROP COLUMN total_weighted_score;
	ALTER TABLE users
	    DROP COLUMN weight_total;
END $$
DELIMITER ;
