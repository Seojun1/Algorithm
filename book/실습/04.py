# 문자열 바꾸기 (a:b:c:d --> a#b#c#d)
a = 'a:b:c:d'
a = a.split(':')
print('#'.join(a))