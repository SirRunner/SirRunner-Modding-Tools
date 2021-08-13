from collections import deque

test_file = "C:/Program Files (x86)/Steam/steamapps/common/Victoria 2/mod/TTA/decisions/Erebor.txt"


class Node:
    """When name == None, it is a comment Node"""
    def __init__(self, name, value, level):
        self._name = name
        if isinstance(value, list):
            self._values = list(value)
        else:
            self._values = [value]
        self._level = level

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        self._values = list(values)

    def append(self, value):
        self._values.append(value)

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    def __str__(self):
        ret_str = "\n"
        tabs = "\t" * self._level
        ret_str += tabs

        if self._name:
            ret_str += f"{self._name} = "
        else:
            ret_str += "# "

        if isinstance(self._values[0], Node):
            ret_str += "{"

        if self._values[0]:
            for value in self._values:
                ret_str += str(value)
        else:
            ret_str += "{}"

        if isinstance(self._values[0], Node):
            ret_str += "\n" + tabs + "}"

        return ret_str

    def __repr__(self):
        return self.__str__()


class Decision:
    def __init__(self, name, potential, allow, effect):
        self._name = name
        self._potential = potential
        self._allow = allow
        self._effect = effect

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def potential(self):
        return self._potential

    @potential.setter
    def potential(self, potential):
        self._potential = potential

    @property
    def allow(self):
        return self._allow

    @allow.setter
    def allow(self, allow):
        self._allow = allow

    @property
    def effect(self):
        return self._effect

    @effect.setter
    def effect(self, effect):
        self._effect = effect

    def __str__(self):
        ret_str = f"\t{self.name} = {{"
        ret_str += str(self._potential) + "\n"
        ret_str += str(self._allow) + "\n"
        ret_str += str(self._effect) + "\n"
        ret_str += "\t}\n"

        return ret_str

    def __repr__(self):
        return self.__str__()


class PoliticalDecisions:
    def __init__(self, decision_list):
        self.decisions = list(decision_list)

    def __str__(self):
        ret_str = "political_decisions = {\n"

        for decision in self.decisions:
            ret_str += str(decision)

        ret_str += "}"
        return ret_str

    def __repr__(self):
        return self.__str__()


def generate_section(q, level, previous=None):
    test = q.pop()

    if test == "}":
        return previous
    else:
        q.append(test)

    name = q.pop()
    second = q.pop()
    third = q.pop()

    if second == "=" and third == "{":
        value = generate_section(q, level+1)
        test = q.pop()
        if test != "}":
            q.append(test)
        return Node(name, value, level)
    elif second == "=" and third == "{}":
        return Node(name, None, level)
    elif second == "=" and third != "{":
        if not previous:
            previous = list()
        previous.append(Node(name, third, level))
        return generate_section(q, level, previous)
    elif second != "=":
        return SyntaxError(f"File is not formatted correctly: {name}, {second}, {third}")


def make_decisions(q):
    decisions = []
    while len(q) != 1:  # only works when there is one political_decisions block
        name = q.pop()
        q.pop()
        q.pop()
        potential = generate_section(q, 2)
        allow = generate_section(q, 2)
        effect = generate_section(q, 2)
        decisions.append(Decision(name, potential, allow, effect))
    return decisions


parts = deque()
with open(test_file) as infile:
    for line in infile:
        split_line = line.split("#")
        code = split_line[0].strip()

        for section in code.split():
            last = None
            if '=' in section and len(section) != 1:
                split_section = section.split("=")
                for item in split_section:
                    if item == "" and last != "=":
                        parts.appendleft("=")
                        last = "="
                    elif item != split_section[-1]:
                        parts.appendleft(item)
                        parts.appendleft("=")
                        last = "="
                    elif item != "":
                        parts.appendleft(item)
                        last = item
            else:
                parts.appendleft(section)
                last = section

# while parts:
#     print(parts.pop())

item = parts.pop()
file = None
if item == "political_decisions":
    parts.pop()
    parts.pop()
    decisions = make_decisions(parts)
    file = [PoliticalDecisions(decisions)]
    for p_block in file:
        print(p_block)
