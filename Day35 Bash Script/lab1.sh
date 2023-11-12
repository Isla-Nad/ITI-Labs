sed -n '/lp/p' /etc/passwd
sed  '3d' /etc/passwd 
sed  '$d' /etc/passwd
sed '/lp/d' /etc/passwd
sed -i 's/lp/mylp/g' pass
==========================================
awk -F: '{ print $5 }' /etc/passwd
awk -F: '{ print NR,$5,":",$6 }' /etc/passwd
awk -F: '{ if ($3 > 500) print $1,$3,$5 }' /etc/passwd
awk -F: '{ if ($3 == 500) print $1,$3,$5 }' /etc/passwd
awk '{ if (NR>=5 && NR<=15) print NR":::"$0 }' /etc/passwd
awk '{ if(gsub("lp", "mylp")) print $0 }' /etc/passwd
awk -F: '{ if ($3 > max) { max = $3; line = $0 } } END {print line}' /etc/passwd
awk -F: '{ sum += $3 } END { print sum }' /etc/passwd
awk -F: '{ sum[$4] += $3 }END {for (g in sum) print g ,sum[g]}' /etc/passwd
awk -F: 'BEGIN {print "User-Group Report\n--------------------------"} 
               {users[$4] = users[$4] $1 "\n"}
         END { for (g in users) {
                  print "Group" g " Name:"
                  print users[g]
             }
        }' /etc/passwd
==========================================