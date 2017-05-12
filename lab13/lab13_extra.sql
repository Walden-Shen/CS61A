.read lab13.sql

-- A table with the following columns:
--   word
--   category
--   dependency_type
--   dependent_category
--   count - Number of occurrences of the combination of
--           (word, category, dependency_type, dependent_category)
--   frequency - For given word-category pair, the number of occurrences of
--               (word, category, dependency_type, dependent_category) combination
--               divided by the number occurences overall of the word-category pair
CREATE TABLE IF NOT EXISTS frequencies AS
    SELECT c.word as word, c.category as category, c.dependency_type as dependency_type, c.dependent_category as dependent_category,
           COUNT(*) as count, COUNT(*) * 1.0/count.count as frequency
    FROM deps as c, word_cat_count as count
    WHERE c.word = count.word AND c.category = count.category
    GROUP BY c.word, c.category, c.dependency_type, c.dependent_category;

-- In case we have to reconstruct the table

-- For each word-category pair, what is the most likely dependent category?
-- Dependent category cannot be punctuation (i.e. dependent_category != "F")
-- The observed frequency of the dependent should be greater than 0.5
-- The number of occurrences of the word-category pair should be greater than 10
CREATE TABLE likeliest_child AS
    -- REPLACE THIS LINE
    select 'YOUR CODE HERE';
