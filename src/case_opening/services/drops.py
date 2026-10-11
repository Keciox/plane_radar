from random import randint,SystemRandom,choices


test = {"AK-47 Grotto":1000,"AWP dragon lore":70000}

def drop_random(pairs: dict[str,int]):
    drop = choices(list(pairs.keys()),weights=list(pairs.values()),k=1)
    print(drop)





def random_float():
    pass

drop_random(test)