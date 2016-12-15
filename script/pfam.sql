-- Pfam stuff
DROP TABLE IF EXISTS pfam;
CREATE TABLE pfam (
	id TEXT,
	pfam_acc TEXT,
	clan_id TEXT,
	pfam_id TEXT,
	pfam_desc TEXT
);

CREATE INDEX ix_pfam ON pfam (id_pfam, pfam_acc, clan_id, pfam_id);

-- Taxonomy thing
-- Inspire by http://stackoverflow.com/questions/4240433/creating-taxonomy-table-in-mysql
CREATE TABLE taxonomic_units (
	id INT, 
	
)
