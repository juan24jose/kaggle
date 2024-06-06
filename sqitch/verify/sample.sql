-- verify/sample_table.sql

-- Verify that the sample_table table exists
SELECT EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_name = 'sample_table'
) AS table_exists;
