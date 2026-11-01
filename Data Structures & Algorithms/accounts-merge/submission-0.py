class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
    
    def find(self, n1):
        res = n1
        while res!=self.parent[res]:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]
        return res

    def union(self, a, b):
        p1, p2 = self.parent[a], self.parent[b]
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]: # a is the bigger component
            self.rank[p1]+=self.rank[p2]
            self.parent[p2] = p1
        else:
            self.rank[p2]+=self.rank[p1]
            self.parent[p1] = p2
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        1. standard union find on accounts to identify duplicates
        parent: account indexes
        rank: connected account components

        2. Data processing on inputs to get it into the required shape.
        - emailAccounts -> {email: accIndex}
        union(a,b) if an email was seen before
        set email to the find(account)
        else: record the current account as the owner
        
        3. for each email: find the accindex and find the root from parent. For each root, append the emails
        4. Construct the result. For each group, sort email and prepend the account name
        '''
        n = len(accounts)
        uf = UnionFind(n)
        emailAccounts = {}

        # construct email -> account 
        # union if emails exists
        for acc, emails in enumerate(accounts):
            for email in emails[1:]:
                if email not in emailAccounts:
                    emailAccounts[email] = acc
                else:
                    # the accounts are duplicate
                    uf.union(acc, emailAccounts[email])
        
        # construct account -> list of emails
        new_accounts = defaultdict(list)
        for email, account in emailAccounts.items():
            leader = uf.find(account)
            new_accounts[leader].append(email)

        res = []
        for acc, emails in new_accounts.items():
            res.append([accounts[acc][0]] + emails)
        
        return res

        


        





        