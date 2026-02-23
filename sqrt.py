odd = 1
        count = 0
        
        while x >= odd:
            x -= odd
            odd += 2
            count += 1
        
        return count