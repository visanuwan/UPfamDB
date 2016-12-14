CREATE TABLE pfam (
	id_pfam TEXT,
	pfam_acc TEXT,
	clan_id TEXT,
	pfam_id TEXT,
	pfam_desc TEXT
);

CREATE INDEX ix_pfam ON pfam (id_pfam, pfam_acc, clan_id, pfam_id);
