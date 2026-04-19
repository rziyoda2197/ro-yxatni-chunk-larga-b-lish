def chunk_list(input_list, chunk_size):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

# Misol:
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
print(chunk_list(input_list, chunk_size))
```

Kodni ishga tushirish uchun, siz input_list ro'yxatiga va chunk_size o'lchamiga qiymat berishingiz kerak. Natijada, chunk_size o'lchamiga bo'lingan ro'yxat chiqadi.
