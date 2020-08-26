HParse x.txt x.net
sed 's=!NULL=<eps>=' x.net > x.net2
python3 parse.py x.net2 > x.dot
dot -Tpng x.dot -o x.png
shotwell x.png
