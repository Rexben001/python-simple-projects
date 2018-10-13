class Ben:
    def __init__(self, name, age):
        self.names = name
        self.ages = age
    def desc(self):
        return self.names
    def says(self, hey):
        return self.hey
named = Ben('Me', 12)

print(named.names,'is', named.ages)
print('My name is ', named.desc())
n = Ben(12,33)
print('Hello',n.says('mr'))
