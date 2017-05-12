"""Representations of an IULA-format dependency treebank."""

def tree_from_row_list(rows):
    """Assumes the schema in the IULA database. Returns the root of the tree."""
    id_to_tree = {row.id: Tree(row) for row in rows}
    for row_id, row_tree in id_to_tree.items():
        if row_tree.row.head == 0: # This row is the root
            root = row_tree
        else:
            row_tree.set_parent(id_to_tree[row_tree.row.head])
    return root

class Tree:
    def __init__(self, row):
        self.branches = []
        self.row = row

    def set_parent(self, parent=None):
        assert isinstance(parent, Tree)
        self.parent = parent
        self.parent.branches.append(self)

    def deps(self):
        """Yield each node's information for the deps table."""
        for branch in self.branches:
            yield self.row.base_form, self.row.simplified_category, \
                    branch.row.base_form, branch.row.simplified_category, branch.row.deprel
            for child_record in branch.deps():
                yield child_record

    def as_string(self, indent=0):
        str_list = [" " * indent + "(" + str(self.row)]
        for branch in self.branches:
            str_list.append(branch.as_string(indent + 2))
        str_list.append(" " * indent + ')')
        return "\n".join(str_list)

class Leaf:
    def __init__(self, tag, word):
        self.tag = tag
        self.word = word

class Row:
    def __init__(self, database_str):
        self.database_str = database_str.strip()
        obj_list = self.database_str.split('\t')
        self.id = int(obj_list[0])
        self.form = obj_list[1]
        self.base_form = obj_list[2]
        self.ccategory = obj_list[3]
        self.category = obj_list[4]
        self.parse_feats(obj_list[5])
        self.head = int(obj_list[6])
        self.deprel = obj_list[7]
        self.simplify_category()
        # For now, ignore the last two columns about "projective head"

    def parse_feats(self, feat_string):
        if feat_string == "_":
            self.feats = None
        else:
            bindings = feat_string.split("|")
            self.feats = {}
            for binding in bindings:
                key, value = binding.split("=")
                self.feats[key] = value

    def simplify_category(self):
        """Adds a simplified_category attribute depending on the fine POS category."""
        if self.category[0] in ("D", "N", "P", "C"):
            self.simplified_category = self.category[:2]
        elif self.category[0] == "V":
            self.simplified_category = self.category[:3]
        else:
            self.simplified_category = self.category[0]

    def __str__(self):
        return self.database_str

