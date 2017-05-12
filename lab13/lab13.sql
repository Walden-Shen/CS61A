-- Read from the database file spanish.db
.open spanish.db

-- Remove any tables created by a previous execution of this file
DROP TABLE IF EXISTS masculine_a;
DROP TABLE IF EXISTS category_counts;
DROP TABLE IF EXISTS word_cat_count;
DROP TABLE IF EXISTS noun_verbs;
DROP TABLE IF EXISTS likeliest_child;

-- A table containing words that are masculine but end in "a"
CREATE TABLE masculine_a as
    -- REPLACE THIS LINE
    select 'YOUR CODE HERE';

-- A table containing each word, category, and count of that group
CREATE TABLE word_cat_count AS
    -- REPLACE THIS LINE
    select 'YOUR CODE HERE';

-- A table containing all info of words that can be both nouns and verbs
CREATE TABLE noun_verbs AS
    -- REPLACE THIS LINE
    select 'YOUR CODE HERE';
