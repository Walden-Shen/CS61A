"""Count words and rules from a Treebank."""

from tree import tree_from_row_list, Row

import sqlite3
import sys

def read_trees(source):
    """Yield all trees in SOURCE."""
    tree_rows = []
    for line in source:
        if line == '\n':
            yield tree_from_row_list(tree_rows)
            tree_rows = []
        else:
            tree_rows.append(Row(line))

def tree_records(filename):
    """Yield database rows from all trees in file FILENAME."""
    with open(filename, 'r', encoding="utf-8") as f:
        for tree in read_trees(f):
            for record in tree.deps():
                yield record

def generate_table(srcfile, destfile):
    """Read a SRCFILE in CONLL format and write a table to DESTFILE."""
    conn = sqlite3.connect(destfile)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS deps")
    c.execute("CREATE TABLE deps ("
              "word TEXT,"
              "category TEXT,"
              "dependent_word TEXT,"
              "dependent_category TEXT,"
              "dependency_type TEXT)")
    c.executemany("INSERT INTO deps VALUES (?, ?, ?, ?, ?)",
                  tree_records(srcfile))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    import time
    start_time = time.time()
    print("Building spanish.db...")
    generate_table("data_spanish.conll", "spanish.db")
    print("Total execution time: {0} seconds".format(time.time() - start_time))

