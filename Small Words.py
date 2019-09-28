def small_words(arr):
    
    for i in arr:
        
        if len(i)<=3:
            
            yield i
