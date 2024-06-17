seq = [1]
n = 2
k = 3

past_lt = []

# Replace "while True" to "while your_number not in seq" if you want continue cycle before your_number in seq
# Example:
# while 3 not in seq:
while True:
    chain_exists = True
    if seq[-1]:
        if sum(seq[-k:]) // k != seq[-1]:
            chain_exists = False
         
        if chain_exists:
            seq[-k:] = [seq[-1] + 1] * 2
            n += 2
            
            if not (n in past_k or n == k):
                k = n
                past_lt += [seq[-1]]
        else:
            if seq[-1] == 1 or n == 1:
                seq[-1:] = [seq[-1] - 1] * (n)
            else:
                seq[-1:] = [seq[-1] - 1] * (n - 1)
    else:
        n **= (len(seq) + 1)
        seq[seq.index(0):] = [1,1]
        n += 2
            
    print(seq, n, k)
        
            
                
            
